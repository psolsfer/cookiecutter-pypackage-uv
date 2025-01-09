"""
Tasks for maintaining the {{ cookiecutter.project_name }} package.

Execute 'invoke --list' for guidance on using Invoke
"""

import logging
import os
import platform
import shutil
import webbrowser
from pathlib import Path

from invoke.context import Context
from invoke.exceptions import Failure
from invoke.runners import Result
from invoke.tasks import task

logger = logging.getLogger(__name__)

ROOT_DIR = Path(__file__).parent
TEST_DIR = ROOT_DIR.joinpath("tests")
SOURCE_DIR = ROOT_DIR.joinpath("src/{{ cookiecutter.project_slug }}")
TOX_DIR = ROOT_DIR.joinpath(".tox")
COVERAGE_FILE = ROOT_DIR.joinpath(".coverage")
COVERAGE_DIR = ROOT_DIR.joinpath("htmlcov")
COVERAGE_REPORT = COVERAGE_DIR.joinpath("index.html")
DOCS_DIR = ROOT_DIR.joinpath("docs")
DOCS_BUILD_DIR = DOCS_DIR.joinpath("site")
DOCS_INDEX = DOCS_BUILD_DIR.joinpath("index.html")
PYTHON_DIRS = [str(d) for d in [SOURCE_DIR, TEST_DIR]]


def _delete_file(file: Path) -> None:
    file.unlink(missing_ok=True)

def _run(c: Context, command: str, ignore_failure: bool = False) -> Result | None:
    try:
        return c.run(f"uv run {command}", pty=platform.system() != "Windows")
    except Failure:
        if ignore_failure:
            return None
        raise


# Lint, formatting, type checking
@task
def type_check(c: Context, ignore_failure: bool = False) -> None:
    """Type checking with mypy."""
    _run(c, "mypy --junit-xml reports/mypy.xml .", ignore_failure)


@task(help={"check": "Only checks without making changes (bool)"})
def lint_ruff(c: Context, check: bool = True, ignore_failure: bool = False) -> None:
    """Check style with Ruff."""
    check_str = "--no-fix" if check else ""
    _run(c, "ruff check {} {}".format(check_str, " ".join(PYTHON_DIRS)), ignore_failure)
{%- if cookiecutter.formatter|lower == 'black' %}


@task(help={"check": "Only checks without making changes"})
def format_black(c: Context, check = True, ignore_failure: bool = False) -> None:
    """Check style with black."""
    check_str = "--check" if check else ""
    _run(c, "black --check {} {}".format(check_str, " ".join(PYTHON_DIRS)), ignore_failure)
{%- elif cookiecutter.formatter|lower == 'ruff-format' %}


@task(help={"check": "Only checks without making changes (bool)"})
def format_ruff(c: Context, check: bool = True, ignore_failure: bool = False) -> None:
    """Check style with Ruff Formatter."""
    check_str = "--check" if check else ""
    _run(c, "ruff format {} {}".format(check_str, " ".join(PYTHON_DIRS)), ignore_failure)
{%- endif %}


@task(help={"check": "Only checks, without making changes"})
def lint(c: Context, check: bool = True) -> None:
    """Run all linting/formatting."""
    lint_ruff(c, check, True)
    {%- if cookiecutter.formatter|lower == 'black' %}
    format_black(c, check, True)
    {%- elif cookiecutter.formatter|lower == 'ruff-format' %}
    format_ruff(c, check, True)
    {%- endif %}
    type_check(c, True)


# Tests
@task(help={"tox_env": "Environment name to run the test"})
def test(c: Context, tox_env: str = "py311") -> None: # TODO Should be the highest supported py ver
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
    {%- if cookiecutter.use_pytest == 'y' %}
    _run(c, f"coverage run --source {SOURCE_DIR} -m pytest")
    {%- else %}
    _run(c, f"coverage run --source {SOURCE_DIR} uv run pytest")
    {%- endif %}
    _run(c, "coverage report")
    if publish:
        # Publish the results via coveralls
        _run(c, "coveralls")
    else:
        # Build a local report
        _run(c, "coverage html")
        webbrowser.open(COVERAGE_REPORT.as_uri())
{%- if cookiecutter.development_environment == "strict" %}


@task
def safety(c: Context) -> None:
    """Check safety of the dependencies."""
    _run(c, "safety check --continue-on-error --full-report")
{%- endif %}
{%- if cookiecutter.with_jupyter_lab == "y" %}


# Jupyter lab
@task
def lab(c: Context) -> None:
    """Run Jupyter lab."""
    _run(c, "mkdir -p notebooks")
    _run(c, "jupyter lab --allow-root --notebook-dir notebooks")
{%- endif %}


# Documentation
@task(help={"launch": "Launch documentation in the web browser"})
def docs(c: Context, launch: bool = True) -> None:
    """Generate documentation."""
    # Remove old documentation files
    clean_docs(c)
    # Generate documentation
    _run(c, "mkdocs build")
    if launch:
        webbrowser.open(DOCS_INDEX.as_uri())


@task
def deploy_docs(c: Context) -> None:
    """Deploy documentation."""
    _run(c, "mkdocs gh-deploy")


@task
def servedocs(c: Context) -> None:
    """Serve the docs with live reloading."""
    _run(c, "mkdocs serve")


# Clean
@task
def clean_build(c: Context) -> None:
    """Clean up files from package building."""
    for dirpath in ["build", "dist", ".eggs"]:
        shutil.rmtree(dirpath, ignore_errors=True)
    for pattern in ["*.egg-info", "*.egg"]:
        for filename in Path().glob('**/' + pattern):
            if filename.is_dir():
                shutil.rmtree(filename, ignore_errors=True)
            else:
                filename.unlink(missing_ok=True)


@task
def clean_python(c: Context) -> None:
    """Clean up python file artifacts."""
    for pattern in ["*.pyc", "*.pyo", "*~", "__pycache__"]:
        for filename in Path().glob('**/' + pattern):
            try:
                if filename.is_file():
                    filename.unlink(missing_ok=True)
                elif filename.is_dir():
                    shutil.rmtree(filename)
            except OSError as e:
                logger.warning("Failed to remove %s: %s", filename, e.strerror)


@task
def clean_tests(c: Context) -> None:
    """Clean up files from testing."""
    _delete_file(COVERAGE_FILE)
    shutil.rmtree(TOX_DIR, ignore_errors=True)
    shutil.rmtree(COVERAGE_DIR, ignore_errors=True)


@task
def clean_docs(c: Context) -> None:
    """Clean up files from documentation builds."""
    shutil.rmtree(DOCS_BUILD_DIR, ignore_errors=True)


@task(pre=[clean_build, clean_python, clean_tests, clean_docs])
def clean(c: Context) -> None:
    """Run all clean sub-tasks."""


# Build and release
@task
def pre_release_check(c: Context) -> None:
    """Complete before releasing the package."""
    lint(c, True)
    test_all(c)


@task(clean)
def dist(c: Context) -> None:
    """Build source and wheel packages."""
    _run(c, "uv build")


@task(dist)
def release(c: Context) -> None:
    """Make a release of the python package to pypi."""
    _run(c, "uv publish")


# Package installation
@task(clean)
def install_package(c: Context) -> None:
    """Install the package to the active Python's site-packages."""
    _run(c, "uv sync")


@task
def pre_commit_install(c: Context) -> None:
    """Install pre-commit hooks."""
    _run(c, "pre-commit install")


@task(pre=[install_package, pre_commit_install])
def install(c: Context) -> None:
    """Install the package and the pre-commit hooks."""

# pipx

@task
def install_pipx(c: Context) -> None:
    """Download and install pipx."""
    if os.name == "nt":  # Windows
        c.run("py -m pip install pipx")
    else:  # Unix/Linux/MacOS
        c.run("python3 -m pip install pipx")


# uv
@task
def install_uv(c: Context) -> None:
    """Download and install uv."""
    if os.name == "nt":  # Windows
        c.run("powershell -ExecutionPolicy ByPass -c 'irm https://astral.sh/uv/install.ps1 | iex'")
    else:  # Unix/Linux/MacOS
        c.run("curl -LsSf https://astral.sh/uv/install.sh | sh")


# @task
# def remove_uv(c: Context) -> None:
#     """Uninstall uv."""
#     if os.name == "nt":  # Windows
#         c.run(
#             "(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py -UseBasicParsing).Content | py - --uninstall"
#         )
#     else:  # Unix/Linux/MacOS
#         c.run(
#             "curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python3 - --uninstall"
#         )
