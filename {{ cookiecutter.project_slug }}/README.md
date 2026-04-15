# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

[![License](https://img.shields.io/badge/license-{{ cookiecutter.license.replace('-', '--') }}-blue)](LICENSE)
[![Tests](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions/workflows/ci.yml/badge.svg)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions)
[![Docs](https://img.shields.io/badge/docs-mkdocs-blue)](https://{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.project_slug }}/)

---

## Installation

```bash
pip install {{ cookiecutter.project_slug }}
```

Or with uv:

```bash
uv pip install {{ cookiecutter.project_slug }}
```

## Quick Start

```python
from {{ cookiecutter.package_name }} import example_function

result = example_function(5.0)
print(result)  # 25.0
```

---

## Development

```bash
# Clone the repository
git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.git
cd {{ cookiecutter.project_slug }}

# Install with dev dependencies
uv pip install -e ".[dev]"

# Run tests
pytest

# Run linting
ruff check .
ruff format .
mypy src/
```

---

## License

{{ cookiecutter.license }} — see [LICENSE](LICENSE).
