# ARCHITECTURE — statpkg-template

> **Status: Architecture stub.** Full design after `pyrbmi` v0.5.0 (by which point the template can be extracted from lived experience).

---

## 1. Template Engine

**Cookiecutter** (`cookiecutter ≥ 2.6`) with a `cookiecutter.json` prompting for:

```json
{
  "project_name": "my-stat-package",
  "package_name": "my_stat_package",
  "author_name": "",
  "license": ["Apache-2.0", "MIT"],
  "python_requires": ">=3.11",
  "r_reference_package": "",
  "cran_task_view": ["Survival", "ClinicalTrials", "Epidemiology", "TimeSeries", "Econometrics", "Bayesian", "Other"],
  "include_joss_paper": true,
  "include_rpy2_validation": true,
  "include_benchmarks": true
}
```

---

## 2. CRAN Task View → PyPI Classifier Mapping

The template auto-populates `pyproject.toml` classifiers that mirror CRAN Task View categories, enabling PyPI search to surface statistical packages by domain — a discoverability gap currently unfilled.

| CRAN Task View | PyPI Classifier (proposed) |
|---|---|
| ClinicalTrials | `Topic :: Scientific/Engineering :: Medical Science Apps` |
| Survival | `Topic :: Scientific/Engineering :: Bio-Informatics` |
| Epidemiology | `Topic :: Scientific/Engineering :: Medical Science Apps` |
| Econometrics | `Topic :: Scientific/Engineering :: Mathematics` |
| TimeSeries | `Topic :: Scientific/Engineering :: Mathematics` |
| Bayesian | `Topic :: Scientific/Engineering :: Artificial Intelligence` |

---

## 3. Validation Scaffold

`validation/compare_r.py` — generated stub:

```python
"""
Compare {package_name} output against R package {r_reference_package}.
Run with: uv run python validation/compare_r.py
Requires: rpy2 (uv add rpy2 --dev)
"""
import rpy2.robjects as ro
# ... scaffold to be filled by package author
```

---

## 4. JOSS Paper Template

`paper/paper.md` generated with all required JOSS sections pre-populated:
- Summary
- Statement of Need (includes R parity rationale boilerplate)
- Mathematics (LaTeX)
- Citations (`.bib` with R reference package pre-cited)
- Acknowledgements
