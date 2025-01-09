# Console Script Setup

----

Optionally, your package can include a console script using Click, Typer or argparse.

## How It Works

If the 'command_line_interface' option is set to ['click'], ['typer'] or ['argparse'] during setup, cookiecutter will add a file 'cli.py' in the project_slug subdirectory. An entry point is added to pyproject.toml that points to the main function in cli.py.

## Usage

To use the console script in development:

```bash linenums="0"
uv sync
```

The script will be generated with output for no arguments and --help.

Executing:

```bash linenums="0"
project_slug --help
```

shows help about the package.

## More Details

Click the links to obtain more information about [Typer](https://typer.tiangolo.com/) and [Click](http://click.pocoo.org/).
