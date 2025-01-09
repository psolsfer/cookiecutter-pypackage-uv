# Prompts

----

When you create a package, you are prompted to enter these values.

## Templated Values

The following appear in various parts of your generated project.

/// define
`full_name`

- Your full name.

`email`

- Your email address

`github_username`

- Your GitHub username.

`project_name`

- The name of your new Python package project. This is used in documentation, so spaces and any characters are fine here. [Check the availability](http://ivantomic.com/projects/ospnc/) of possible names before creating the project.

`project_slug`

- The namespace of your Python package. This should be Python import-friendly. Typically, it is the slugified version of `project_name`. Note: your PyPi project will use `project_slug`, so change those in the README.md file afterwards.

`project_short_description`

- A one-sentence description of what your Python package does.

`pypi_username`

- Your Python Package Index account username.

`private_package_repository_name`

- Optional name of a private package repository to install packages from and publish this package to.

`private_package_repository_url`

- Optional URL of a private package repository to install packages from and publish this package to. Make sure to include the /simple suffix. For instance, when using a GitLab Package Registry this value should be of the form <https://gitlab.com/api/v4/projects/> {project_id} /packages/pypi/simple.

`version`

- The starting version number of the package.

`python_version`

- Python version of the package.
///

## Options

The following package configuration options set up different features for your project.

/// define
`use_pytest`

- Whether to use [pytest](https://docs.pytest.org/en/latest/)

``formatter``

- Whether a formatter is used or not. Options: ['Black', 'Ruff-format', 'No']. Note that the Ruff formater is still experimental. For more information see [Ruff formatter](https://github.com/astral-sh/ruff/blob/main/crates/ruff_python_formatter/README.md)

``docs``

- Whether to initialize documentation, and where to host it. Options: ['Read the Docs', 'Github Pages', 'No']

``development_environment``

- Whether to configure the development environment with a focus on simplicity or with a focus on strictness. In strict mode, additional are added, and tools such as Mypy and Pytest are set to strict mode. Options: ['simple', 'strics']

``with_jupyter_lab``

- Adds to JupyterLab to uv's dev dependencies, and an Invoke's task to start Jupyter Lab in the `notebooks/` directory.

``with_pydantic_typing``

Use pydantic's mypy plugin

``command_line_interface``

- Whether to create a console script using Click, Typer or argparse. Console script entry point will match the project_slug. Options: ['No command-line interface', 'Click', 'Typer', 'Argparse']

``create_author_file``

- Whether to create an authors file

``docstring_style``

- Select the style of the docstrings. Options: ['numpy', 'Google']

``open_source_license``

- Choose a [license](https://choosealicense.com/). Options: ['BSD-3-Clause', 'MIT', 'ISC', 'Apache-2.0', 'GPL-3.0-only', 'Not open source' ]

///
