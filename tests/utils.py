"""Utils for testing."""

import os
import shlex
import shutil
import subprocess
from collections.abc import Generator
from contextlib import contextmanager
from pathlib import Path
from typing import Any

import pytest
from cookiecutter.utils import rmtree
from pytest_cookies.plugin import Cookies, Result


@pytest.fixture(scope="session")
def prebuilt_env(tmp_path_factory: pytest.TempPathFactory) -> Generator[Path, None, None]:
    """Create and share a prebuilt environment for all tests that need it."""
    venv_dir = tmp_path_factory.mktemp("venv")

    # Find the full path to 'uv'
    uv_path = shutil.which("uv")
    if uv_path is None:
        msg = "uv executable not found in PATH"
        raise RuntimeError(msg)

    try:
        # Create venv and install dependencies
        subprocess.check_call(["uv", "venv", str(venv_dir)])
        subprocess.check_call([uv_path, "sync", "--all-extras"])  # Create the environment
        yield venv_dir
    finally:
        shutil.rmtree(venv_dir)


def run_inside_venv(command: str, venv_dir: Path, dirpath: Path | str) -> int:
    """Run a command inside the prebuilt virtual environment."""
    venv_bin = Path(venv_dir) / "bin"

    env: dict[str, str] = os.environ.copy()
    env["PATH"] = f"{venv_bin}:{env['PATH']}"  # Prepend venv bin to PATH
    env["UV_PROJECT_ENVIRONMENT"] = str(venv_dir)  # uv uses the prebuilt virtual environment
    env["UV_LINK_MODE"] = "symlink"  # Faster, if not "hardlink", and last option "copy"
    env["VIRTUAL_ENV"] = str(venv_dir)  # Override VIRTUAL_ENV to match the project environment

    # FIXME The 'symlinks' are the faster choice. However, is not possible to use them, as it seems
    # that uv cache is in a different drive, so the mode changes to "copy" instead. The code below
    # sets the cache directory, but the files are read only and the test fails.

    # Set UV cache directory to be on the same drive as the project
    # project_cache = Path(dirpath) / ".uv-cache"
    # env["UV_CACHE_DIR"] = str(project_cache)

    with inside_dir(dirpath):
        result = subprocess.run(
            shlex.split(command),
            env=env,
            capture_output=True,
            text=True,
        )
        # Those give some output with "pytest -s"
        # print(f"\nresult.stdout:\n{result.stdout}")
        # print(f"\nresult.stderr:\n{result.stderr}")

        return result.returncode


@contextmanager
def inside_dir(dirpath: str | Path) -> Generator[None, None, None]:
    """Execute code from inside the given directory.

    dirpath: str
        Path of the directory the command is being run.
    """
    old_path = Path.cwd()
    try:
        os.chdir(dirpath)
        yield
    finally:
        os.chdir(old_path)


@contextmanager
def bake_in_temp_dir(
    cookies: Cookies, *args: tuple[Any], **kwargs: dict[str, Any]
) -> Generator[Result, Any, Any]:
    """Delete the temporal directory that is created when executing the tests.

    cookies: pytest_cookies.Cookies,
        cookie to be baked and its temporal files will be removed
    """
    result = cookies.bake(*args, **kwargs)
    try:
        yield result
    finally:
        rmtree(str(result.project))


# REMOVE Not used: using run_inside_venv instead, so the venv won't be recreated
def run_inside_dir(command: str, dirpath: str | Path):
    """Run a command from inside a given directory, returning the exit status.

    command:
        Command that will be executed
    dirpath:
        String, path of the directory the command is being run.
    """
    with inside_dir(dirpath):
        return subprocess.check_call(shlex.split(command))


# NOTE Unused
def check_output_inside_dir(command: str, dirpath: str | Path):
    """Run a command from inside a given directory, returning the command output."""
    with inside_dir(dirpath):
        return subprocess.check_output(shlex.split(command))


def project_info(result: Result):
    """Get toplevel dir, project_slug, and project dir from baked cookies."""
    project_path = Path(result.project)
    project_slug = os.path.split(project_path)[-1]
    project_dir = Path(project_path) / "src" / project_slug
    return project_path, project_slug, project_dir
