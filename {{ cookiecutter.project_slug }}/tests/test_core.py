"""Tests for core module."""
import pytest
from hypothesis import given, strategies as st

from {{ cookiecutter.package_name }}.core import example_function


def test_example_function_basic():
    """Test example_function with basic inputs."""
    assert example_function(2.0) == 4.0
    assert example_function(0.0) == 0.0
    assert example_function(-3.0) == 9.0


@given(st.floats(allow_nan=False, allow_infinity=False))
def test_example_function_non_negative(x):
    """Property-based test: result is always non-negative."""
    result = example_function(x)
    assert result >= 0
    assert isinstance(result, float)
