# Contributing to {{ cookiecutter.project_name }}

Thank you for your interest in contributing!

## Development Setup

1. Fork and clone the repository
2. Install dependencies: `uv pip install -e ".[dev]"`
3. Install pre-commit hooks: `pre-commit install`

## Pull Request Process

1. Create a feature branch: `git checkout -b feature/my-feature`
2. Make your changes with tests
3. Ensure all tests pass: `pytest`
4. Run linting: `ruff check . && ruff format . && mypy src/`
5. Commit with conventional commits (enforced by pre-commit)
6. Push and create a pull request

## Code Style

- **Ruff** for linting and formatting
- **MyPy** for type checking (strict mode)
- **NumPy docstring** convention
- **Conventional commits** for commit messages

## Testing

- All code must have unit tests
- Use **Hypothesis** for property-based tests where applicable
- Aim for high test coverage

## Questions?

Open an issue or discussion on GitHub.
