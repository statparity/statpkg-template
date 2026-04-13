# statpkg-template

**Cookiecutter template for JOSS-ready Python statistical packages — closing the CRAN publication pipeline gap.**

[![License](https://img.shields.io/badge/license-Apache--2.0-blue)](LICENSE)

---

## Motivation

R's CRAN ecosystem publishes 100–180 new statistical packages per month, the majority implementing methods directly from peer-reviewed papers. Python has no equivalent publication pipeline: PyPI has no review process, no enforced documentation standards, and no discoverability layer comparable to CRAN Task Views.

`statpkg-template` provides a standardized scaffold that makes publishing a Python statistical package — from paper implementation to PyPI + JOSS — as frictionless as authoring an R package for CRAN.

---

## What It Generates

```
my-stat-package/
├── src/my_stat_package/   # Main source (uv/src layout)
├── tests/                 # pytest + hypothesis property tests
├── docs/                  # MkDocs + mkdocstrings
├── paper/                 # JOSS paper.md + paper.bib
├── benchmarks/            # ASV or pytest-benchmark
├── validation/            # Reference implementation comparisons (rpy2 or manual)
├── .github/workflows/     # CI (lint, test, matrix), release, docs
├── pyproject.toml         # Complete: ruff, mypy, pytest config
├── README.md
├── ARCHITECTURE.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE                # Apache-2.0 default
└── TODO.md
```

---

## Key Features

- **JOSS-ready**: includes `paper/paper.md` template with all required sections
- **CRAN Task View mapping**: `pyproject.toml` classifiers map to CRAN Task View categories for cross-ecosystem discoverability
- **Validation-first**: `validation/` directory with `rpy2`-based comparison scaffold
- **uv-native**: full `uv` workflow, no `setup.py`, no `requirements.txt`
- **Hypothesis integration**: property-based test scaffold for statistical correctness
- **SemVer-gated**: pre-commit hooks enforce conventional commits → auto-changelog

---

## License

Apache-2.0 — see [LICENSE](LICENSE).
