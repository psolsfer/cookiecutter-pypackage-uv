"""Tests to check that the project is properly baked."""

import importlib
import os
import sys
from datetime import UTC, datetime
from pathlib import Path
from unittest import mock

import pytest
from click.testing import CliRunner as ClickCliRunner
from pytest_cookies.plugin import Cookies
from typer.testing import CliRunner as TyperCliRunner

from tests.utils import bake_in_temp_dir, prebuilt_env, project_info, run_inside_venv

if sys.version_info < (3, 11):
    from tomli import load as toml_load
else:
    from tomllib import load as toml_load

INTERFACES = ["No command-line interface", "Click", "Typer", "Argparse"]

# FIXME The tests "test_bake_and_run_and_invoke" are slow, because can't use "symlinks",
# so the "copy" mode is going to copy the actual env files


def test_bake_with_defaults(cookies: Cookies):
    """Test the default structure and configuration of the baked project."""
    with bake_in_temp_dir(cookies) as result:
        assert result.project is not None
        assert result.project.isdir()
        assert result.exit_code == 0
        assert result.exception is None

        project_path, project_slug, project_dir = project_info(result)
        assert project_path.name == project_slug == "python_boilerplate"

        assert project_dir.parts[-1] == "python_boilerplate"
        assert project_dir.parts[-2] == "src"
        assert project_dir.parts[-3] == "python_boilerplate"

        found_toplevel_files = [f.basename for f in result.project.listdir()]
        assert "pyproject.toml" in found_toplevel_files
        assert "src" in found_toplevel_files
        assert "tox.ini" in found_toplevel_files
        assert "tests" in found_toplevel_files
        assert "AUTHORS.md" in found_toplevel_files

        doc_files = [f.basename for f in result.project.join("docs").listdir()]
        assert "authors.md" in doc_files

        assert result.project.join("src/python_boilerplate").isdir()


def test_bake_and_run_tests(prebuilt_env: Path, cookies: Cookies):
    """Reuse the prebuilt environment."""
    with bake_in_temp_dir(cookies, extra_context={"use_pytest": "y"}) as result:
        test_file_path = result.project.join("tests/test_python_boilerplate.py")
        lines = test_file_path.readlines()
        assert "import pytest" in "".join(lines)
        assert run_inside_venv("pytest", prebuilt_env, str(result.project)) == 0


def test_year_compute_in_license_file(cookies: Cookies):
    """Test the year in the license file."""
    with bake_in_temp_dir(cookies) as result:
        if result.exception is not None:
            pytest.fail(f"Cookie baking failed: {result.exception}")

        license_path = Path(result.project) / "LICENSE"
        if not license_path.exists():
            pytest.fail("LICENSE file not found in the project directory")

        current_year = str(datetime.now(tz=UTC).astimezone().year)
        assert (
            current_year in license_path.read_text()
        ), f"Year {current_year} not found in LICENSE file"


def test_bake_withspecialchars(cookies: Cookies):
    """Ensure that a `full_name` with double quotes does not break pyproject.toml."""
    with bake_in_temp_dir(cookies, extra_context={"full_name": 'name "quote" name'}) as result:
        assert result.project.isdir()


def test_bake_with_apostrophe(cookies: Cookies):
    """Ensure that a `full_name` with apostrophes does not break pyproject.toml."""
    with bake_in_temp_dir(cookies, extra_context={"full_name": "O'connor"}) as result:
        assert result.project.isdir()


def test_bake_without_author_file(cookies: Cookies):
    """Ensure that the authors files are removed."""
    with bake_in_temp_dir(cookies, extra_context={"create_author_file": "n"}) as result:
        assert result.project is not None
        result.project.listdir()
        found_toplevel_files = [f.basename for f in result.project.listdir()]
        assert "AUTHORS.md" not in found_toplevel_files
        doc_files = [f.basename for f in result.project.join("docs").listdir()]
        assert "authors.md" not in doc_files

        # Assert there are no spaces in the toc tree
        # docs_index_path = result.project.join("docs/index.md")
        # with Path.open(str(docs_index_path)) as index_file:
        #     assert "contributing\n   history" in index_file.read()


def test_bake_selecting_license(cookies: Cookies):
    """Assert that the license is properly set."""
    license_strings = {
        "MIT": "MIT License",
        "BSD-3-Clause": "Redistributions of source code must retain the "
        "above copyright notice, this",
        "ISC": "ISC License",
        "Apache-2.0": "Licensed under the Apache License, Version 2.0",
        "GPL-3.0-only": "GNU GENERAL PUBLIC LICENSE",
    }
    for license_name, target_string in license_strings.items():
        context = {"open_source_license": license_name}
        with bake_in_temp_dir(cookies, extra_context=context) as result:
            # NOTE Path.open won't work properly for python<3.11
            with Path.open(result.project.join("LICENSE"), encoding="utf-8") as f:
                content = f.read()
                assert target_string in content
            with Path.open(result.project.join("pyproject.toml"), encoding="utf-8") as f:
                content = f.read()
                assert license_name in content
            # NOTE the lines below can induce encoding errors
            # assert target_string in result.project.join("LICENSE").read()
            # assert license_name in result.project.join("pyproject.toml").read()


def test_bake_not_open_source(cookies: Cookies):
    """Ensure that license is removed for not open source projects."""
    with bake_in_temp_dir(
        cookies, extra_context={"open_source_license": "Not open source"}
    ) as result:
        found_toplevel_files = [f.basename for f in result.project.listdir()]
        assert "pyproject.toml" in found_toplevel_files
        assert "LICENSE" not in found_toplevel_files
        assert "License" not in result.project.join("README.md").read()


def test_not_using_pytest(cookies: Cookies):
    """Ensure that pytest is not used when 'use_pytest' == 'n'."""
    with bake_in_temp_dir(cookies, extra_context={"use_pytest": "n"}) as result:
        assert result.project.isdir()
        test_file_path = result.project.join("tests/test_python_boilerplate.py")
        lines = test_file_path.readlines()
        assert "import unittest" in "".join(lines)
        assert "import pytest" not in "".join(lines)


@pytest.mark.parametrize("interface", INTERFACES)
def test_bake_with_console_script_files(cookies: Cookies, interface: str):
    """Ensure that the cli is properly set."""
    context = {"command_line_interface": interface}
    result = cookies.bake(extra_context=context)
    project_path, project_slug, project_dir = project_info(result)
    found_project_files = os.listdir(project_dir)

    pyproject_path = project_path / "pyproject.toml"
    with Path.open(pyproject_path, encoding="utf-8") as pyproject_file:
        file_content = pyproject_file.read()

    if interface == "No command-line interface":
        assert "cli.py" not in found_project_files
        assert "[project.scripts]" not in file_content
    else:
        assert "cli.py" in found_project_files
        assert "[project.scripts]" in file_content


def test_bake_with_console_script_cli(cookies: Cookies):
    """Test the baked project's command line interface using Click."""
    context = {"command_line_interface": "Click"}
    result = cookies.bake(extra_context=context)
    project_path, project_slug, project_dir = project_info(result)
    module_path = Path(project_dir) / "cli.py"
    module_name = f"{project_slug}.cli"
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    cli = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(cli)
    runner = ClickCliRunner()
    noarg_result = runner.invoke(cli.main)
    assert noarg_result.exit_code == 0
    noarg_output = f"Replace this message by putting your code into {project_slug}.cli.main"
    assert noarg_output in noarg_result.output
    help_result = runner.invoke(cli.main, ["--help"])
    assert help_result.exit_code == 0
    assert "Show this message" in help_result.output


def test_bake_with_typer_console_script_cli(cookies: Cookies):
    """Test the baked project's command line interface using Typer."""
    context = {"command_line_interface": "Typer"}
    result = cookies.bake(extra_context=context)
    project_path, project_slug, project_dir = project_info(result)
    module_path = Path(project_dir) / "cli.py"
    module_name = f"{project_slug}.cli"
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    cli = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(cli)
    runner = TyperCliRunner()
    noarg_result = runner.invoke(cli.app)
    assert noarg_result.exit_code == 0
    noarg_output = f"Replace this message by putting your code into {project_slug}.cli"
    assert noarg_output in noarg_result.output
    help_result = runner.invoke(cli.app, ["--help"])
    assert help_result.exit_code == 0
    assert "Show this message" in help_result.output


def test_bake_with_argparse_console_script_cli(cookies: Cookies, capsys):
    """Test the baked project's command line interface using argparse."""
    context = {"command_line_interface": "Argparse"}
    result = cookies.bake(extra_context=context)
    project_path, project_slug, project_dir = project_info(result)
    module_path = project_dir / "cli.py"
    module_name = f"{project_slug}.cli"
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    cli = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(cli)

    with mock.patch("argparse._sys.argv", ["cli"]):
        noarg_result = cli.main()
        assert noarg_result == 0
        out, err = capsys.readouterr()
        noarg_output = f"Replace this message by putting your code into {project_slug}.cli.main"
        assert noarg_output in out

    # Mock the command line arguments for --help
    with mock.patch("argparse._sys.argv", ["cli", "--help"]):
        try:
            help_result = cli.main()
        except SystemExit as e:
            help_result = e.code

        assert help_result == 0

        out, err = capsys.readouterr()
        assert "show this help message" in out


@pytest.mark.parametrize("formatter", ["Black", "Ruff-format", "No"])
def test_formatter(cookies: Cookies, formatter: str):
    """Ensure that the chosen formater is properly set."""
    formatter_to_dependency: dict[str, dict[str, str | bool | None]] = {
        "Black": {"dependency": "black", "always_included": False},
        "Ruff-format": {
            "dependency": "ruff",
            "always_included": True,
        },  # Ruff is always a dependency
        "No": {"dependency": None, "always_included": True},
    }
    formatter_to_task: dict[str, str | None] = {
        "Black": "black --check",
        "Ruff-format": "ruff format",
        "No": None,
    }

    with bake_in_temp_dir(cookies, extra_context={"formatter": formatter}) as result:
        assert result.project.isdir()

        # Validate dependencies in `pyproject.toml`
        pyproject_path = result.project.join("pyproject.toml")
        with Path.open(pyproject_path, "rb") as f:
            pyproject_content = toml_load(f)
        dev_dependencies = pyproject_content["dependency-groups"]["dev"]
        # Assert that dependency is in the dev group, and the other don't (except for that are
        # 'always_included')
        for fmt, metadata in formatter_to_dependency.items():
            dep = metadata["dependency"]
            if dep is not None:
                if fmt == formatter or metadata["always_included"]:
                    assert any(dep in d for d in dev_dependencies)
                else:
                    assert not any(dep in d for d in dev_dependencies)

        # Validate tasks in `tasks.py`
        tasks_path = result.project.join("tasks.py")
        tasks_content = tasks_path.read()
        selected_task = formatter_to_task[formatter]

        if formatter == "No":
            # Ensure no formatting tasks are present
            for task in formatter_to_task.values():
                if task is not None:
                    assert task not in tasks_content
        else:
            # Ensure only the selected formatter task is present
            for task in formatter_to_task.values():
                if task is not None:
                    if task == selected_task:
                        assert task in tasks_content
                    else:
                        assert task not in tasks_content


@pytest.mark.parametrize(
    "command",
    [
        "uv run invoke lint",
        "uv run invoke docs --no-launch",
    ],
)
def test_bake_and_run_and_invoke(prebuilt_env: Path, cookies: Cookies, command: str):
    """Run the unit tests of a newly-generated project using invoke's tasks."""
    with bake_in_temp_dir(cookies) as result:
        assert result.project is not None
        assert result.project.isdir()
        return_code = run_inside_venv(command, prebuilt_env, str(result.project))
        assert return_code == 0, f"'{command}' failed with return code {return_code}"
