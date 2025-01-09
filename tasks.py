"""Development tasks for the cookiecutter template project.

Execute 'invoke --list' for guidance on using Invoke
"""

import platform
import shutil
import webbrowser
from pathlib import Path

from invoke.context import Context
from invoke.runners import Result
from invoke.tasks import task

BAKE_OPTIONS = "--no-input"

ROOT_DIR = Path(__file__).parent
COVERAGE_DIR = ROOT_DIR.joinpath("htmlcov")
COVERAGE_REPORT = COVERAGE_DIR.joinpath("index.html")
DOCS_DIR = ROOT_DIR.joinpath("docs")
DOCS_BUILD_DIR = DOCS_DIR.joinpath("site")
DOCS_INDEX = DOCS_BUILD_DIR.joinpath("index.html")
HOOKS_DIR = ROOT_DIR.joinpath("hooks")
TEST_DIR = ROOT_DIR.joinpath("tests")
PYTHON_DIRS = [str(d) for d in [HOOKS_DIR, TEST_DIR]]


def _run(c: Context, command: str) -> Result | None:
    return c.run(f"uv run {command}", pty=platform.system() != "Windows")


@task
def bake(c: Context, _bake_options: str = BAKE_OPTIONS) -> None:
    """Generate project using defaults."""
    _run(c, f"cruft create . --config-file {_bake_options}")


@task
def watch(c: Context, _bake_options: str = BAKE_OPTIONS) -> None:
    """Generate project using defaults and watch for changes."""
    bake(c, _bake_options)
    _run(
        c,
        "watchmedo shell-command -p '*.*' -c 'invoke bake --_bake_options={_bake_options}' -W -R -D {{cookiecutter.project_slug}}/",
    )


@task
def replay(c: Context) -> None:
    """Replay last cookiecutter run and watch for changes."""
    watch(c, bake_options="--replay")


@task
def docs(c: Context) -> None:
    """Generate documentation."""
    # Remove old documentation files
    clean_docs(c)
    # Generate docs
    _run(c, "mkdocs build")
    webbrowser.open(DOCS_INDEX.absolute().as_uri())


@task
def clean_docs(c: Context) -> None:
    """Clean up files from documentation builds."""
    shutil.rmtree(DOCS_BUILD_DIR, ignore_errors=True)


# Lint, formatting, type checking
@task
def type_check(c: Context) -> None:
    """Type checking with mypy."""
    _run(c, "mypy --junit-xml reports/mypy.xml .")


@task(help={"check": "Only checks without making changes"})
def lint_ruff(c: Context, check: bool = True) -> None:
    """Check style with Ruff."""
    check_str = "--no-fix" if check else ""
    _run(c, "ruff check {} {}".format(check_str, " ".join(PYTHON_DIRS)))


@task(help={"check": "Only checks without making changes"})
def format_ruff(c: Context, check: bool = True) -> None:
    """Check style with Ruff Formatter."""
    check_str = "--check" if check else ""
    _run(c, "ruff format {} {}".format(check_str, " ".join(PYTHON_DIRS)))


@task(help={"check": "Only checks, without making changes"})
def lint(c: Context, check: bool = True) -> None:
    """Run all linting/formatting."""
    lint_ruff(c, check)
    format_ruff(c, check)
    type_check(c)


# Tests
@task(help={"tox_env": "Environment name to run the test"})
def test(c: Context, tox_env: str = "py311") -> None:
    """Run tests with tox."""
    _run(c, f"tox -e {tox_env}")


@task
def test_pytest(c: Context) -> None:
    """Run tests quickly with the default Python."""
    _run(c, "pytest")


@task
def test_all(c: Context) -> None:
    """Run tests on every Python version with tox."""
    _run(c, "tox")


@task(help={"publish": "Publish the result via coveralls"})
def coverage(c: Context, publish: bool = False) -> None:
    """Run tests and generate a coverage report."""
    _run(c, "coverage run")
    _run(c, "coverage report")
    if publish:
        # Publish the results via coveralls
        _run(c, "coveralls")
    else:
        # Build a local report
        _run(c, "coverage html")
        webbrowser.open(COVERAGE_REPORT.as_uri())


@task
def safety(c: Context) -> None:
    """Check safety of the dependencies."""
    _run(c, "safety check --continue-on-error --full-report")
