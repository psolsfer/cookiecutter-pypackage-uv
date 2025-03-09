#!/usr/bin/env python

"""Tests for `{{ cookiecutter.project_name }}` package."""

{% if cookiecutter.command_line_interface|lower == "argparse" -%}
import argparse
{% endif -%}
{% if cookiecutter.use_pytest == "y" -%}

import pytest
{% else -%}
import unittest
{% endif -%}

{% if cookiecutter.command_line_interface|lower == "click" -%}
from click.testing import CliRunner
{% elif cookiecutter.command_line_interface|lower == "typer" -%}
import re
from typer.testing import CliRunner
{% endif -%}

from {{ cookiecutter.project_slug }} import {{ cookiecutter.project_slug }}
{% if cookiecutter.command_line_interface|lower in ["click", "argparse"] -%}
from {{ cookiecutter.project_slug }} import cli
{% elif cookiecutter.command_line_interface|lower == "typer" -%}
from {{ cookiecutter.project_slug }}.cli import app
{% endif -%}

{% if cookiecutter.use_pytest == "y" -%}
@pytest.fixture
def response() -> None:
    """Sample pytest fixture."""
    # import requests
    # return requests.get("https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}")"""

def test_content(response) -> None:
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert "GitHub" in BeautifulSoup(response.content).title.string
{% if cookiecutter.command_line_interface|lower == "click" -%}

def test_command_line_interface() -> None:
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert "{{ cookiecutter.project_slug }}.cli.main" in result.output
    help_result = runner.invoke(cli.main, ["--help"])
    assert help_result.exit_code == 0
    assert "--help  Show this message and exit." in help_result.output
{% elif cookiecutter.command_line_interface|lower == "typer" -%}

def test_command_line_interface() -> None:
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(app)
    assert result.exit_code == 0
    assert "{{ cookiecutter.project_slug }}.cli.app" in result.output
    help_result = runner.invoke(app, ["--help"])
    assert help_result.exit_code == 0
    assert re.search(r"--help\s+Show this message and exit.", help_result.output) is not None
{% elif cookiecutter.command_line_interface|lower == "argparse" -%}

def test_command_line_interface(capsys) -> None:
    """Test the CLI."""
    from unittest import mock
    import sys

    # Mock the command line arguments
    with mock.patch.object(sys, 'argv', ['cli']):
        result = cli.main()
        assert result == 0

        out, err = capsys.readouterr()
        assert "{{ cookiecutter.project_slug }}.cli.main" in out

    # Mock the command line arguments for --help
    with mock.patch.object(sys, 'argv', ['cli', '--help']):
        try:
            help_result = cli.main()
        except SystemExit as e:
            help_result = e.code

        assert help_result == 0

        out, err = capsys.readouterr()
        assert "--help  Show this message and exit." in out
{% endif -%}
{% else -%}

class Test{{ cookiecutter.project_slug|title }}(unittest.TestCase):
    """Tests for `{{ cookiecutter.project_slug }}` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""
{% if cookiecutter.command_line_interface|lower == "click" -%}

    def test_command_line_interface(self) -> None:
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert "{{ cookiecutter.project_slug }}.cli.main" in result.output
        help_result = runner.invoke(cli.main, ["--help"])
        assert help_result.exit_code == 0
        assert "--help  Show this message and exit." in help_result.output
{% elif cookiecutter.command_line_interface|lower == "typer" -%}

    def test_command_line_interface(self) -> None:
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(app)
        assert result.exit_code == 0
        assert "{{ cookiecutter.project_slug }}.cli.app.main" in result.output
        help_result = runner.invoke(app, ["--help"])
        assert help_result.exit_code == 0
        assert re.search(r"--help\s+Show this message and exit.", help_result.output) is not None
{% endif -%}
{% endif -%}
