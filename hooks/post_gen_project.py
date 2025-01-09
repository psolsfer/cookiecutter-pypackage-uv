"""Run after the project is generated."""

#!/usr/bin/env python
import shutil
import textwrap
from pathlib import Path

PROJECT_DIRECTORY = Path.cwd()
PROJECT_NAME = "{{ cookiecutter.project_name }}"
PROJECT_SLUG = "{{ cookiecutter.project_slug }}"
GITHUB_USER = "{{ cookiecutter.github_username }}"
create_author_file = "{{ cookiecutter.create_author_file }}"
command_line_interface = "{{ cookiecutter.command_line_interface|lower }}"
open_source_license = "{{ cookiecutter.open_source_license }}"
documentation = "{{ cookiecutter.docs|lower }}"


def _remove_file(filepath: Path | str):
    if isinstance(filepath, str):
        filepath = Path(filepath)
    (PROJECT_DIRECTORY / filepath).unlink()


def _remove_folder(folderpath: Path | str):
    if isinstance(folderpath, str):
        folderpath = Path(folderpath)
    shutil.rmtree(folderpath, ignore_errors=True)


def print_final_instructions(project: str, github_user: str) -> None:
    """Print further instructions after the project was created.

    Parameters
    ----------
    project : str
        Name of the project
    github_user : str
        Github user
    """
    message = f"""
    Your project {project} has been created.

    1) Now you can start working on it:

        $ cd {project} && git init

    2) If you don't have uv installed run:

        $ invoke install-uv

        (Use 'invoke --list' for all available tasks)

    3) Initialize uv and install pre-commit hooks:

        $ invoke install

    4) Upload initial code to GitHub:

        $ git add .
        $ git commit -m ":tada: Initial commit"
        $ git branch -M main
        $ git remote add origin https://github.com/{github_user}/{project}.git
        $ git push -u origin main

    Note: If you don't have Invoke installed and wish to use it, create a virtual environment and install it:

        $ pip install virtualenv
        $ cd your_project_directory
        $ virtualenv env
        $ source env/bin/activate (or .\\env\\Scripts\\activate on Windows)
        $ pip install invoke
    """
    print(textwrap.dedent(message))


if __name__ == "__main__":
    if create_author_file != "y":
        _remove_file("AUTHORS.md")
        _remove_file("docs/authors.md")

    if "no" in command_line_interface:
        cli_file = Path("src") / PROJECT_SLUG / "cli.py"
        _remove_file(cli_file)

    if open_source_license == "Not open source":
        _remove_file("LICENSE")

    if "no" in documentation:
        _remove_folder("/docs")

    if "read" not in documentation:
        _remove_file(".readthedocs.yaml")

    print_final_instructions(project=PROJECT_NAME, github_user=GITHUB_USER)
