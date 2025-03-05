# Contributing

----

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

You can contribute in many ways:

## Types of Contributions

### Report Bugs

Report bugs at [Issues].

If you are reporting a bug, please include:

- Your operating system name and version.
- Any details about your local setup that might be helpful in troubleshooting.
- Detailed steps to reproduce the bug.

### Fix Bugs

Look through the GitHub issues for bugs. Anything tagged with "bug" and "help
wanted" is open to whoever wants to implement it.

### Implement Features

Look through the GitHub issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

### Write Documentation

{{ cookiecutter.project_name }} could always use more documentation, whether as part of the
official docs, in docstrings, or even on the web in blog posts,
articles, and such.

### Submit Feedback

The best way to send feedback is to file an issue at [Issues].

If you are proposing a feature:

- Explain in detail how it would work.
- Keep the scope as narrow as possible, to make it easier to implement.
- Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

### Get Started

Ready to contribute? Here's how to set up `{{ cookiecutter.project_slug }}` for local development.

1. Fork the `{{ cookiecutter.project_slug }}` repo on GitHub.
2. Clone your fork locally:

    ```bash linenums="0"
    git clone <git@github.com>:your_name_here/{{ cookiecutter.project_slug }}.git
    ```

3. Set up your local copy with uv.

    First, navigate to your project directory:

    ```bash linenums="0"
    cd {{ cookiecutter.project_slug }}/
    ```

    Then, create a new virtual environment and install the dependencies:

    ```bash linenums="0"
    uv sync
    ```

    This will create a new virtual environment (if one doesn’t already exist) and install the project dependencies

4. Create a branch for local development:

    ```bash linenums="0"
    git checkout -b name-of-your-bugfix-or-feature
    ```

    Note that this project has branch protection set up through pre-commit hooks. Direct commits to `main` and `staging` branches are prevented to maintain code quality and ensure proper review.

5. Now you can make your changes locally.

6. After making your changes, ensure that they pass all tests. This includes testing compatibility with different Python versions using `tox`. You can run all tests with the following command:

    ```bash linenums="0"
    invoke test-all
    ```

    Next, verify that your changes adhere to the established coding style guidelines. This can be done by running the linting command:

    ```bash linenums="0"
    invoke lint
    ```

    This command will check your code for any style issues and provide feedback on any discrepancies found. It’s crucial to maintain consistent coding style for readability and maintainability of the project."

7. Commit your changes and push your branch to GitHub:

=== "using commitizen"
    ```bash
    git add .
    uv run cz commit
    git push origin name-of-your-bugfix-or-feature
    ```

=== "manual commits"
    ```bash linenums="0"
    git add .
    git commit -m "Your detailed description of your changes."
    git push origin name-of-your-bugfix-or-feature
    ```

8. Submit a pull request through the GitHub website.

9. After your PR is merged, you can safely delete your branch:
   ```bash
   git checkout main
   git pull  # Get the latest changes including your merge
   git branch -d name-of-your-bugfix-or-feature
   ```

This workflow keeps the repository history clean and organized.

### Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.md.
3. The pull request should work for Python 3.10, and 3.11, and for PyPy. Check "<span>https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions</span>" and make sure that the tests pass for all supported Python versions.

### Tips

To run a subset of tests:

{% if cookiecutter.use_pytest == 'y' -%}
```bash linenums="0"
pytest tests.test_{{ cookiecutter.project_slug }}
```
{% else -%}
```bash linenums="0"
python -m unittest tests.test_{{ cookiecutter.project_slug }}
```
{%- endif -%}

### Deploying

A reminder for the maintainers on how to deploy.

1. Update `HISTORY.md` file with the changes made for the new release.

2. Commit the changes

    Committing changes to your version control system is a crucial part of every release. It ensures that every change is tracked and can be reverted if necessary.

    The recommended option is to use [Commitizen], a tool designed to help teams adhere to a standard commit message format. This standard format can then be used by tools like automated changelog generators and version bumpers.

    Here’s how you can use Commitizen to commit your changes:

    ```bash linenums="0"
    uv run cz commit
    ```

    When you run this command, Commitizen will prompt you to fill out a commit message in a specific format. This format typically includes the type of change (e.g., feature, bugfix), a short description, and optionally a longer description and any breaking changes.

    If you’re not using Commitizen, you can manually add and commit your changes with Git:

    ```bash linenums="0"
    git add .
    git commit -m "Changelog for upcoming release 0.1.1."
    ```

    Remember, it’s important to write clear and descriptive commit messages that accurately represent your changes.

3. Update version number

    The version number of your package is a crucial piece of information that helps users and contributors understand the current state of your project. It’s important to update the version number whenever you make a significant change to your project. For more information see [SemVer].

    The recommended method for updating the version number is to use [Commitizen]:

    ```bash linenums="0"
    uv run cz bump
    ```

    When you run this command, Commitizen will bump your project’s version according to the changes that have been made since the last release. It determines the type of version bump (major, minor, or patch) based on the commit messages. This is why it’s important to follow a standard commit message format.

    This command will also update the version in several files accross the project. These files must be defined in the `version_files` list under the `[tool.commitizen]` section in `pyproject.toml`.

    If you are not using Commitizen, you can manually update the version number using [uv] (the new version can be 'major', 'minor', or 'patch'):

    ```bash linenums="0"
    uv version minor
    ```

    However, note that while this will update the version in `pyproject.toml`, it won’t update the version strings in other files.

4. Install the package for local development

    After updating the version number, it’s important to install the package again for local development. This is because the version number is often used in the package’s metadata, and installing the package ensures that this metadata is updated.

    When you install a Python package for local development using uv, it’s installed in editable mode. This means that changes to the source code will be immediately available in your environment, without needing to reinstall the package.

    Here’s how you can install the package for local development with uv:

    ```bash linenums="0"
    uv sync
    ```

    This command will install your package in editable mode, along with its dependencies.

5. Run the tests

    Run the tests Before pushing your changes to ensure that your package is working as expected:

    === ":octicons-zap-24: Invoke"

        ```bash linenums="0"
        invoke test-all
        ```

    === ":simple-uv: uv"

        ```bash linenums="0"
        uv run tox
        ```

        or

        ```bash linenums="0"
        uv run pytest
        ```

6. Push the commit

    After confirming that everything is working, push your commit to the remote repository:

    ```bash linenums="0"
    git push
    ```

7. Push the tags

    Pushing tags is crucial for creating a new release on both GitHub and PyPI. This step assumes that you’ve already created a tag for the new release (**see step 3** above):

    ```bash linenums="0"
    git push --tags
    ```

Github Actions will then deploy to [PyPI] if tests pass.

[Issues]: <https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/issues>
[Commitizen]: http://commitizen.github.io/cz-cli/
[PyPI]: https://pypi.org/
[SemVer]: https://semver.org/
