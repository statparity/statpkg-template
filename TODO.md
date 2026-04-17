# TODO — statpkg-template

> **Status: Milestone stub.** Full atomization after `pyrbmi` v0.5.0.

---

## Phase 0 — Setup
- [x] 0.1 Initialize cookiecutter repo (`uv init statpkg-template`)
- [x] 0.2 Add `LICENSE` (Apache-2.0)
- [x] 0.3 CI: test template generation end-to-end on cookiecutter

## v0.1.0 — Base Template
- [x] 1.1 `cookiecutter.json` with all prompts (project name, license, CRAN Task View, JOSS flag)
- [x] 1.2 `src/` layout generation with `uv`-native `pyproject.toml`
- [x] 1.3 GitHub Actions CI template (lint → typecheck → test matrix)
- [x] 1.4 GitHub Actions release template (tag `v*` → PyPI publish)
- [x] 1.5 MkDocs + mkdocstrings site template
- [x] 1.6 `CHANGELOG.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md` templates

## v0.2.0 — Validation Scaffold
- [x] 2.1 `validation/compare_r.py` — rpy2-based comparison scaffold
- [x] 2.2 `validation/fixtures/` directory with README explaining fixture format
- [x] 2.3 Pre-commit hooks: conventional commits, ruff, mypy

## v0.3.0 — JOSS Paper Template
- [ ] 3.1 `paper/paper.md` with all required JOSS sections pre-populated
- [ ] 3.2 `paper/paper.bib` with R reference package pre-cited
- [ ] 3.3 GitHub Actions: JOSS paper build check (compile on PR)

## v0.4.0 — CRAN Task View Classifier Mapping
- [ ] 4.1 Auto-populate PyPI `pyproject.toml` classifiers from CRAN Task View selection
- [ ] 4.2 Draft PyPI classifier proposal for statistical sub-domains (separate RFC)

## v0.5.0 — Hypothesis + Benchmark Scaffold
- [ ] 5.1 Property-based test scaffold (`hypothesis`) for statistical correctness
- [ ] 5.2 `benchmarks/` scaffold with `pytest-benchmark` or `asv`

## v1.0.0 — Stable + User Guide
- [ ] 6.1 Full user guide: "From paper to PyPI in a day"
- [ ] 6.2 Worked example: use template to publish a minimal stats package end-to-end
- [ ] 6.3 Announce on PyPI, Discourse, pharmastat/epi mailing lists
