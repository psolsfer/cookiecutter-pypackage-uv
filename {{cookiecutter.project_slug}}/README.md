# {{ cookiecutter.project_name }}

----

{% set license = cookiecutter.open_source_license -%}
{% set is_open_source = cookiecutter.open_source_license != "Not open source" -%}
{% if "read" in cookiecutter.docs|lower -%}
    {% set docs = "read" -%}
{% elif "github" in cookiecutter.docs|lower -%}
    {% set docs = "git" -%}
{% else -%}
    {% set docs = "no" -%}
{% endif -%}
{% if is_open_source -%}
| | |
| --- | --- |
{% if docs != "no" -%}
| **Docs** |{%- if docs == "read" %} [![Documentation Status](<https://readthedocs.org/projects/{{ cookiecutter.project_slug }}/badge/?version=stable> 'Documentation Status')](<https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io/en/stable/>){%- elif docs == "git" %} [![Documentation Status](<https://{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.project_slug }}/> 'Documentation Status')](<https://{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.project_slug }}/>){%- endif %} |{%- endif %}
{%- if not cookiecutter.private_package_repository_name %}
| **Package** | [![PyPI - Version](<https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg?logo=pypi&label=PyPI&logoColor=gold>)](<https://pypi.python.org/pypi/{{ cookiecutter.project_slug }}>) [![PyPI - Downloads](<https://img.shields.io/pypi/dm/{{ cookiecutter.project_slug }}.svg?color=blue&label=Downloads&logo=pypi&logoColor=gold>)](<https://pypi.python.org/pypi/{{ cookiecutter.project_slug }}>) [![PyPI - Python Version](<https://img.shields.io/pypi/pyversions/{{ cookiecutter.project_slug }}.svg?logo=python&label=Python&logoColor=gold>)](<https://pypi.python.org/pypi/{{ cookiecutter.project_slug }}>) |{%- endif %}
| **CI/CD** | [![CI - Test](<https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions/workflows/test-push-pr.yml/badge.svg>)](<https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions/workflows/test-push-pr.yml>) [![CD - Build](<https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions/workflows/python-publish.yml/badge.svg>)](<https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions/workflows/python-publish.yml>) |
| **GitHub** |  [![{{ cookiecutter.project_name }}](https://img.shields.io/badge/GitHub-{{ cookiecutter.project_name|slugify(separator='_') }}-blue.svg)](<https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}>) [![Forks](https://img.shields.io/github/forks/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.svg)](<https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}>) [![Stars](https://img.shields.io/github/stars/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.svg)](<https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}>) [![Issues](https://img.shields.io/github/issues/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.svg)](<https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}>) |
| **Code style** | [![linting - Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff) {%- if cookiecutter.formatter|lower == 'black' %} [![code style - Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) {%- elif cookiecutter.formatter|lower == 'ruff-format' %} [![code style - Ruff formatter](https://img.shields.io/badge/Ruff%20Formatter-checked-blue.svg)](https://github.com/astral-sh/ruff) {%- endif %} [![types - Mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/) |
| **License** | [![License - {{ license }}](<https://img.shields.io/pypi/l/{{ cookiecutter.project_slug }}.svg>)](<https://spdx.org/licenses/{{ license }}.html>) |
{%- endif %}

{{ cookiecutter.project_short_description }}

## Features

TODO

## Credits

This package was created with [Cookiecutter] / [Cruft] and the [Cookiecutter PyPackage uv] project template.

[Cookiecutter]: https://github.com/audreyr/cookiecutter
[Cruft]: https://github.com/cruft/cruft
[Cookiecutter PyPackage uv]: https://github.com/psolsfer/cookiecutter-pypackage-uv
