"""Validation scaffold for comparing Python implementations against R reference.

This module provides utilities for comparing statistical results between
Python implementations and R reference packages using rpy2.

Example usage:
    >>> from validation.compare_r import RComparator
    >>> comparator = RComparator()
    >>> python_result = my_statistical_function(data)
    >>> r_result = comparator.run_r_function("stats", "t.test", data)
    >>> comparator.assert_close(python_result, r_result, rtol=1e-5)

"""

from __future__ import annotations

from typing import Any
from pathlib import Path
import json

import numpy as np
import pandas as pd

# rpy2 is optional - import error handling allows template to work without it
try:
    import rpy2.robjects as ro
    from rpy2.robjects import numpy2ri, pandas2ri
    from rpy2.robjects.packages import importr
    RPY2_AVAILABLE = True
    # Activate automatic conversion
    numpy2ri.activate()
    pandas2ri.activate()
except ImportError:
    RPY2_AVAILABLE = False
    ro = None


class RComparator:
    """Compare Python statistical results against R reference implementations.

    Parameters
    ----------
    fixtures_dir : str or Path, optional
        Directory containing validation fixtures. Defaults to "validation/fixtures".

    Attributes
    ----------
    fixtures_path : Path
        Resolved path to fixtures directory.
    stats : rpy2 package
        Imported R stats package (if rpy2 available).

    Examples
    --------
    >>> comparator = RComparator()
    >>> data = [1, 2, 3, 4, 5]
    >>> r_mean = comparator.run_r_base("mean", data)
    >>> print(r_mean)  # Should match np.mean(data)

    """

    def __init__(self, fixtures_dir: str | Path | None = None) -> None:
        """Initialize comparator with fixtures directory."""
        if not RPY2_AVAILABLE:
            raise ImportError(
                "rpy2 is required for R comparison. "
                "Install with: uv pip install rpy2"
            )

        if fixtures_dir is None:
            self.fixtures_path = Path(__file__).parent / "fixtures"
        else:
            self.fixtures_path = Path(fixtures_dir)

        # Ensure fixtures directory exists
        self.fixtures_path.mkdir(parents=True, exist_ok=True)

        # Import commonly used R packages
        self.stats = importr("stats")
        self.base = importr("base")

    def run_r_function(
        self,
        package: str,
        function: str,
        *args: Any,
        **kwargs: Any,
    ) -> Any:
        """Run an R function from a specified package.

        Parameters
        ----------
        package : str
            Name of R package (e.g., "stats", "lme4", "survival").
        function : str
            Name of function to call.
        *args : Any
            Positional arguments to pass to R function.
        **kwargs : Any
            Keyword arguments to pass to R function.

        Returns
        -------
        Any
            Result from R function, converted to Python types.

        Examples
        --------
        >>> comparator = RComparator()
        >>> result = comparator.run_r_function("stats", "t.test", [1, 2, 3, 4, 5])

        """
        try:
            r_pkg = importr(package)
        except Exception as e:
            raise ImportError(f"Failed to import R package '{package}': {e}")

        r_func = getattr(r_pkg, function)
        result = r_func(*args, **kwargs)
        return result

    def run_r_base(self, function: str, *args: Any, **kwargs: Any) -> Any:
        """Run a function from R's base package.

        Parameters
        ----------
        function : str
            Name of base R function.
        *args : Any
            Positional arguments.
        **kwargs : Any
            Keyword arguments.

        Returns
        -------
        Any
            Result from R function.

        """
        r_func = getattr(self.base, function)
        return r_func(*args, **kwargs)

    def load_fixture(self, name: str) -> dict[str, Any]:
        """Load a validation fixture from JSON.

        Parameters
        ----------
        name : str
            Name of fixture file (without .json extension).

        Returns
        -------
        dict
            Fixture data containing 'input', 'expected', and metadata.

        """
        fixture_path = self.fixtures_path / f"{name}.json"
        with open(fixture_path, "r") as f:
            return json.load(f)

    def save_fixture(
        self,
        name: str,
        input_data: dict[str, Any],
        expected_output: dict[str, Any],
        description: str,
        source: str,
    ) -> None:
        """Save a validation fixture to JSON.

        Parameters
        ----------
        name : str
            Name for the fixture file.
        input_data : dict
            Input parameters for the test.
        expected_output : dict
            Expected output from reference implementation.
        description : str
            Description of what this fixture tests.
        source : str
            Citation or source of the reference values.

        """
        fixture = {
            "description": description,
            "source": source,
            "input": input_data,
            "expected": expected_output,
        }
        fixture_path = self.fixtures_path / f"{name}.json"
        with open(fixture_path, "w") as f:
            json.dump(fixture, f, indent=2, default=str)

    def assert_close(
        self,
        python_result: float | np.ndarray | pd.DataFrame,
        r_result: Any,
        rtol: float = 1e-5,
        atol: float = 1e-8,
        message: str = "",
    ) -> None:
        """Assert that Python and R results are numerically close.

        Parameters
        ----------
        python_result : float, np.ndarray, or pd.DataFrame
            Result from Python implementation.
        r_result : Any
            Result from R implementation.
        rtol : float, default=1e-5
            Relative tolerance for comparison.
        atol : float, default=1e-8
            Absolute tolerance for comparison.
        message : str, optional
            Additional message for assertion failure.

        Raises
        ------
        AssertionError
            If results differ beyond tolerance.

        """
        # Convert R result to numpy/pandas as needed
        if hasattr(r_result, "rx2"):  # R list
            r_converted = {key: np.array(r_result.rx2(key)) for key in r_result.names}
        else:
            try:
                r_converted = np.asarray(r_result)
            except Exception:
                r_converted = r_result

        if isinstance(python_result, pd.DataFrame):
            python_array = python_result.values
        elif isinstance(python_result, np.ndarray):
            python_array = python_result
        else:
            python_array = np.array([python_result])

        if isinstance(r_converted, dict):
            # Handle R list result (like t.test output)
            for key, expected in r_converted.items():
                actual = python_result if not isinstance(python_result, dict) else python_result.get(key)
                np.testing.assert_allclose(
                    actual, expected,
                    rtol=rtol, atol=atol,
                    err_msg=f"{message} - Field '{key}' mismatch"
                )
        else:
            try:
                r_array = np.asarray(r_converted)
                np.testing.assert_allclose(
                    python_array, r_array,
                    rtol=rtol, atol=atol,
                    err_msg=message,
                )
            except AssertionError as e:
                raise AssertionError(
                    f"Python result: {python_result}\nR result: {r_result}\n{e}"
                )


def validate_against_r(
    py_func: callable,
    r_package: str,
    r_function: str,
    fixture_name: str | None = None,
    rtol: float = 1e-5,
) -> None:
    """Convenience function to validate Python function against R.

    Parameters
    ----------
    py_func : callable
        Python function to validate.
    r_package : str
        R package containing reference implementation.
    r_function : str
        R function name.
    fixture_name : str, optional
        Name of fixture to use. If None, calls py_func with default args.
    rtol : float, default=1e-5
        Relative tolerance for comparison.

    """
    comparator = RComparator()

    if fixture_name:
        fixture = comparator.load_fixture(fixture_name)
        inputs = fixture["input"]
        expected = fixture["expected"]
    else:
        # Default test with simple data
        inputs = {"data": [1, 2, 3, 4, 5]}
        expected = None

    # Run Python function
    py_result = py_func(**inputs)

    # Run R function
    r_result = comparator.run_r_function(
        r_package, r_function,
        *inputs.values()
    )

    # Compare
    comparator.assert_close(py_result, r_result, rtol=rtol)
    print(f"✓ Validation passed: {py_func.__name__} matches {r_package}::{r_function}")


if __name__ == "__main__":
    # Example: validate a simple mean calculation
    comparator = RComparator()
    data = [1.0, 2.0, 3.0, 4.0, 5.0]

    python_mean = np.mean(data)
    r_mean = comparator.run_r_base("mean", data)

    print(f"Python mean: {python_mean}")
    print(f"R mean: {r_mean}")
    comparator.assert_close(python_mean, r_mean)
    print("✓ Mean validation passed!")
