# Cookiecutter PyPackage uv

----

| | |
| --- | :---: |
| **Docs** | [![Documentation Status](<https://readthedocs.org/projects/cookiecutter-pypackage-uv/badge/?version=stable> 'Documentation Status')](https://cookiecutter-pypackage-uv.readthedocs.io/en/stable/) |
| **GitHub** | [![Cookiecutter PyPackage uv project](https://img.shields.io/badge/GitHub-Cookiecutter%20PyPackage%20uv-blue.svg)](<https://github.com/psolsfer/cookiecutter-pypackage-uv>) [![Forks](https://img.shields.io/github/forks/psolsfer/cookiecutter-pypackage-uv.svg)](<https://github.com/psolsfer/cookiecutter-pypackage-uv>) [![Stars](https://img.shields.io/github/stars/psolsfer/cookiecutter-pypackage-uv.svg)](<https://github.com/psolsfer/cookiecutter-pypackage-uv>) [![Issues](https://img.shields.io/github/issues/psolsfer/cookiecutter-pypackage-uv.svg)](<https://github.com/psolsfer/cookiecutter-pypackage-uv>)
| **Code style** | [![linting - Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff) [![code style - Ruff formatter](https://img.shields.io/badge/Ruff%20Formatter-checked-blue.svg)](https://github.com/astral-sh/ruff) [![types - Mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)
| **License** | [![License - BSD-3-Clause](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](<https://spdx.org/licenses/BSD-3-Clause.html>) |


[Cookiecutter] / [Cruft] template for a Python package.

## Quickstart

```bash
# Install Cruft (recommended)
uv tool install cruft

# Create a new project
cruft create https://github.com/psolsfer/cookiecutter-pypackage-uv

# Navigate to your new project
cd myproject

# Initialize the project
uv sync

# Start developing!
```

## Features

### Project Setup and Management

- [Cruft]: Keep your project templates up-to-date and track template changes
- [uv]: Modern, fast dependency management and packaging tool for Python
- Integrated GitHub Actions workflows for testing, drafting release notes, and publishing to [PyPI] when a release is created
- Project structure following best practices

### Code Quality Assurance

- [Pre-commit]: Managing and maintaining multi-language pre-commit hooks to ensure code quality
- [Ruff]: Fast Python linter and formatter, combining multiple linting tools
- Alternative formatter option with [Black]
- Static type checking with [Mypy] and data validation using [Pydantic]
- Automatic dependency updates with [Dependabot]

### Testing

- Testing setup with ``unittest`` and ``pytest``
- [tox] configuration for testing against multiple Python versions (3.10+)
- Test coverage reporting with [Coverage.py]
- Optional [JupyterLab] integration for exploratory testing and analysis

### Documentation

- Documentation generation with [MkDocs] and the [Material for MkDocs] theme with [PyMdown Extensions].
- Code documentation extraction with [mkdocstrings]
- Support for multiple docstring styles (Google, NumPy)
- Hosting options for [Read the Docs] or [GitHub Pages]

### Versioning and Release Notes

- [Commitizen] integration for standardized commit messages and version management
- Semantic versioning with automatic changelog generation
- Automated release notes drafting with [Release Drafter]
- History tracking and changelog management

### Command Line Interface

- Optional CLI integration using [Click], [Typer], or [argparse]

### Development Tasks

- Task automation with [Invoke] for common development workflows
- Standardized commands for testing, linting, formatting, and documentation
- Simplified package publication and versioning tools

## Usage

For a brief tutorial, refer to the refer to the [Tutorial](docs/tutorial.md) section of the documentation.

The prompts that need to be filled during the creation of the package are described in [Prompts](docs/prompts.md).

## Updating a project

An existing project can be updated to the latest template using:

```bash linenums="0"
cruft update
```

## Credit

The following templates were used as basis and inspiration for the creation of some parts of this template:

- Initial template forked from [audreyfeldroy/cookiecutter-pypackage].
- Implementation of [Invoke] is based in [briggySmalls/cookiecutter-pypackage].
- Use of release drafter, dependabot, and print instructions after the template is created: [TezRomacH/python-package-template].

[audreyfeldroy/cookiecutter-pypackage]: https://github.com/audreyfeldroy/cookiecutter-pypackage
[briggySmalls/cookiecutter-pypackage]: https://github.com/briggySmalls/cookiecutter-pypackage
[TezRomacH/python-package-template]: https://github.com/TezRomacH/python-package-template

[argparse]: https://docs.python.org/3/library/argparse.html
[Black]: https://black.readthedocs.io/en/stable/
[Click]: https://click.palletsprojects.com/en/stable/
[Coverage.py]: https://coverage.readthedocs.io/
[Commitizen]: https://commitizen-tools.github.io/commitizen/
[Cookiecutter]: <https://github.com/cookiecutter/cookiecutter>
[Cruft]: <https://github.com/cruft/cruft>
[Dependabot]: https://github.com/marketplace/actions/release-drafter
[Invoke]: https://www.pyinvoke.org/
[JupyterLab]: https://jupyter.org/
[Material for MkDocs]: https://squidfunk.github.io/mkdocs-material/
[MkDocs]: https://www.mkdocs.org/
[Mypy]: https://mypy.readthedocs.io/en/stable/
[Pydantic]: https://docs.pydantic.dev
[Pre-commit]: https://pre-commit.com/
[Read the Docs]: https://readthedocs.org
[Release Drafter]: https://github.com/marketplace/actions/release-drafter
[PyMdown Extensions]: https://facelessuser.github.io/pymdown-extensions
[PyPi]: https://pypi.org/
[Ruff]: https://docs.astral.sh/ruff/
[tox]: https://tox.wiki/
[Typer]: https://typer.tiangolo.com/
[uv]: https://docs.astral.sh/uv/
