# Validation Fixtures

This directory contains validation fixtures for comparing Python implementations against R reference packages.

## Fixture Format

Fixtures are JSON files with the following structure:

```json
{
  "description": "Brief description of what this fixture tests",
  "source": "Citation or source of reference values (e.g., 'R stats::t.test documentation')",
  "input": {
    "data": [1.0, 2.0, 3.0, 4.0, 5.0],
    "alternative": "two.sided"
  },
  "expected": {
    "statistic": 4.2426,
    "p_value": 0.0133,
    "conf_int": [-0.285, 3.885]
  }
}
```

## Fields

- **description**: What test case this fixture represents
- **source**: Reference for the expected values (paper DOI, R documentation, etc.)
- **input**: Parameters to pass to both Python and R implementations
- **expected**: Expected output values from reference implementation

## Naming Conventions

- Use descriptive names: `ttest_one_sample.json`, `lm_simple_regression.json`
- Group related fixtures with prefixes: `survival_kaplan_*.json`
- Include edge cases: `*_edge_empty.json`, `*_edge_nan.json`

## Creating Fixtures

### From R

```r
# Run your analysis in R
result <- t.test(c(1, 2, 3, 4, 5))

# Extract key values
cat("statistic:", result$statistic, "\n")
cat("p.value:", result$p.value, "\n")
```

Then manually create JSON with these values, or use the Python comparator:

```python
from validation.compare_r import RComparator

comparator = RComparator()
comparator.save_fixture(
    name="ttest_example",
    input_data={"data": [1, 2, 3, 4, 5]},
    expected_output={"statistic": 4.24, "p_value": 0.013},
    description="One-sample t-test example",
    source="R stats::t.test documentation"
)
```

## Using Fixtures in Tests

```python
from validation.compare_r import RComparator

def test_my_ttest():
    comparator = RComparator()
    fixture = comparator.load_fixture("ttest_one_sample")

    # Run your Python implementation
    result = my_ttest(**fixture["input"])

    # Compare against expected
    assert abs(result.statistic - fixture["expected"]["statistic"]) < 1e-5
```

## Recommended R Packages for Reference

- **stats**: Basic statistical tests (t.test, wilcox.test, etc.)
- **lme4**: Mixed-effects models
- **survival**: Survival analysis (Surv, coxph, survfit)
- **MASS**: Robust statistics, various models
- **sandwich**: Robust standard errors
- **lmtest**: Diagnostic tests for linear models

## References

- R documentation: https://www.rdocumentation.org/
- CRAN Task Views: https://cran.r-project.org/web/views/
- rpy2 documentation: https://rpy2.github.io/
