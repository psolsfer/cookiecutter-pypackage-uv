# Installation

----

## Using Package Managers

To install {{ cookiecutter.project_name }} in your project, choose your preferred package manager:

=== "pip (simple install)"

    ```bash linenums="0"
    pip install {{ cookiecutter.project_slug }}
    ```

    The following [pip guide] can help getting started with [pip] usage.

=== ":simple-uv: uv (recommended for new projects)"

    First, install [uv] if you haven't already (for more detailed instructions refer to [uv installation]):

    ```bash linenums="0"
    # Windows (PowerShell)
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

    # Linux/macOS
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

    Then create and initialize a new project:

    ```bash linenums="0"
    # Create project directory
    mkdir myproject && cd myproject

    # Initialize project with Python 3.12
    uv venv
    uv python install 3.12

    # Install {{ cookiecutter.project_name }}
    uv pip install {{ cookiecutter.project_slug }}
    ```

=== ":simple-poetry: Poetry"
    First, install [Poetry] if you haven't already (for more detailed instructions refer to [Poetry installation]):


    Then create and initialize a new project:

    ```bash linenums="0"
    # Create a new project
    poetry new myproject
    cd myproject

    # Set Python version
    poetry env use 3.12

    # Install {{ cookiecutter.project_name }}
    poetry add {{ cookiecutter.project_slug }}
    ```

## Development Installation

To install {{ cookiecutter.project_name }} for development, you clone the public repository in the [Github repo]:

```bash linenums="0"
git clone git://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}
```

Once you have a copy of the source, you can install it with:

```bash linenums="0"
cd {{ cookiecutter.project_slug }}
uv sync
```

This command installs all dependencies as specified in `pyproject.toml` and also creates a virtual environment if one doesn't exist.

[Github repo]: <https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}>
[pip]: <https://pip.pypa.io/en/stable/>
[pip guide]: <https://pip.pypa.io/en/stable/getting-started/>
[Poetry]: <https://python-poetry.org/>
[Poetry installation]: <https://python-poetry.org/docs/#installation>
[uv]: <https://docs.astral.sh/uv/>
[uv installation]: <https://docs.astral.sh/uv/getting-started/installation/#installation-methods>
