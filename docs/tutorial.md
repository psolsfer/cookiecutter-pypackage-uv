# Tutorial

----

!!! note

    Did you find any of these instructions confusing? [Edit this file](https://github.com/psolsfer/cookiecutter-pypackage-uv/blob/master/docs/tutorial.md) and submit a pull request with your improvements!

To start with, you will need a [GitHub] account and an account on [PyPI]. Create these before you get started on this tutorial. If you are new to Git and GitHub, you should probably spend a few minutes on some of the tutorials at the top of the page at [GitHub Help].

## Step 1: Install Cruft or Cookiecutter

First, you need to create and activate a virtualenv for the package project. Use your favorite method, or create a virtualenv for your new package like this:

```bash linenums="0"
virtualenv ~/.virtualenvs/mypackage
```

Here, `mypackage` is the name of the package that you'll create.

Activate your environment:

```bash linenums="0"
source bin/activate
```

On Windows, activate it like this. You may find that using a Command Prompt window works better than gitbash.

```powershell linenums="0"
> \\path\\to\\env\\Scripts\\activate
```

Install either [Cruft] or [Cookiecutter]

=== ":octicons-project-roadmap-24: Cruft"

    Install [Cruft]:

    ```bash linenums="0"
    pip install cruft
    ```
    or
    ```bash linenums="0"
    uv add cruft
    ```

=== ":simple-cookiecutter: Cookiecutter"

    Install [Cookiecutter]:

    ```bash linenums="0"
    pip install cookiecutter
    ```
    or
    ```bash linenums="0"
    uv add cookiecutter
    ```

## Step 2: Generate Your Package

Now it's time to generate your Python package.

Use either [Cruft] or [Cookiecutter], pointing it at the [cookiecutter-pypackage-uv repo](https://github.com/psolsfer/cookiecutter-pypackage-uv):

=== ":octicons-project-roadmap-24: Cruft"

    ```bash linenums="0"
    cruft create https://github.com/psolsfer/cookiecutter-pypackage-uv
    ```

=== ":simple-cookiecutter: Cookiecutter"

    ```bash linenums="0"
    cookiecutter https://github.com/psolsfer/cookiecutter-pypackage-uv
    ```

You'll be asked to enter a bunch of values to set the package up.
If you don't know what to enter, stick with the defaults.

## Step 3: Initialize uv and Install Pre-commit Hooks

A folder named after the ``[project_slug]`` was created. Move into this folder:

```bash linenums="0"
cd mypackage
```

Now you can initialize [uv], which sets up a new Python environment for your project and creates a `pyproject.toml` file to manage dependencies. You can also install pre-commit hooks, which are scripts that automatically check your code for errors before each commit. The easiest way to achieve this is using the included [Invoke]'s automations:

!!! note

    Your virtualenv should still be activated. If it isn't, activate it now.

/// details | Installing Invoke
    type: tip

If you don't have [Invoke] installed, create a virtual environment and install it:

```bash linenums="0"
pip install virtualenv
cd your_project_directory
virtualenv env
source env/bin/activate (or .\\env\\Scripts\\activate on Windows)
pip install invoke
```

///

```bash linenums="0"
invoke install
```

Alternatively, you can directly use [uv] instead of the automations:

```bash linenums="0"
uv sync
uv pre-commit install
```

The Invoke automations are designed to streamline the installation process by running multiple commands at once. However, if you prefer to have more control over the installation process or if you’re not planning to use Invoke for other tasks, you might find it simpler to use uv directly. Refer to the [Automated tasks](automated_tasks.md) section for more information about the usage of Invoke.

## Step 4: Create a GitHub Repo

Go to your GitHub account and create a new repo named `mypackage`, where `mypackage` matches the `[project_slug]` from your answers to running cruft/cookiecutter.

!!! note

    If your virtualenv folder is within your project folder, be sure to add the virtualenv folder name to your .gitignore file.

Within the project folder, setup git to use your GitHub repo and upload the code:

```bash linenums="0"
git init .
git add .
git commit -m "Initial skeleton."
git remote add origin git@github.com:myusername/mypackage.git
git push -u origin main
```

Where `myusername` and `mypackage` are adjusted for your username and package name.

!!! note

       GitHub has changed the default branch name from 'master' to 'main'. If you are using another Git repository hosting service that uses the Git branch naming defaults, you might need to use 'master' instead of 'main'.

You'll need a ssh key to push the repo. You can [generate] a key or [add] an existing one.

[generate]: https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/
[add]: https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/

## Step 5: Set Up Read the Docs

[Read the Docs] hosts documentation for the open source community. Think of it as Continuous Documentation.

Log into your account at [Read the Docs]. If you don't have one, create one and log into it.

If you are not at your dashboard, choose the pull-down next to your username in the upper right, and select "My Projects". Choose the button to import the repository and follow the directions.

Now your documentation will get rebuilt when you make documentation changes to your package.

## Step 6: Release on PyPI

The Python Package Index or [PyPI] is the official third-party software repository for the Python programming language. Python developers intend it to be a comprehensive catalog of all open source Python packages. For more information, visit the [PyPI release checklist]

When you are ready, release your package the standard Python way. Here's a more detailed [release checklist](pypi_release_checklist.md) you can use.

You can use the Invoke task to publish your package to PyPI:

```bash linenums="0"
invoke release
```

This command will run `uv publish` and upload your package to PyPI.

Alternatively, you have a GitHub workflow (`python-publish.yml`) set up in your project that should automatically publish your package to PyPI when a release is published or a new tag is created.

See [PyPI Help] for more information about submitting a package.

## Having problems?

Visit our [troubleshooting](troubleshooting.md) page for help. If that doesn't help, go to our [Issues] page and create a new Issue. Be sure to give as much information as possible.

[Cookiecutter]: https://cookiecutter.readthedocs.io/
[Cruft]: https://cruft.github.io/cruft/
[GitHub]: https://github.com/
[GitHub Help]: https://help.github.com/
[Invoke]: https://www.pyinvoke.org/
[Issues]: <https://github.com/psolsfer/cookiecutter-pypackage-uv/issues>
[uv]: <https://docs.astral.sh/uv/>
[PyPI]: https://pypi.python.org/pypi
[PyPI Help]: https://pypi.org/help/#publishing
[PyPI release checklist]: pypi_release_checklist.md
[Read the Docs]: <https://readthedocs.org/>
