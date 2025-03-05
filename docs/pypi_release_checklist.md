# PyPI Release Checklist

----

## Before Your First Release

1. **Configure the package**

    In your `pyproject.toml` file, make sure you have specified all the necessary information about your package. This includes the name, version, description, license, authors, and other metadata.

2. **Build the package.**
    Run the following command in your terminal:

    === ":octicons-zap-24: Invoke"

        ```bash linenums="0"
        invoke build
        ```

    === ":simple-uv: uv"

        ```bash linenums="0"
        uv build
        ```

    This will create a distribution package that you can upload to PyPI.

3. **Set up GitHub Actions**

    Ensure that the GitHub Actions workflows are correctly configured in your repository. These workflows automate the testing, building, and publishing process.

4. **Configure environments in GitHub**

    Set up the required environments in your GitHub repository settings:

        - test-pypi (no approval required)
        - pypi (with approval requirements if desired)

5. **Verify the repository secrets**

    Make sure you have correctly set up any required secrets for [PyPI] publishing. With trusted publishing, you typically won't need token secrets.

6. **Publish the package.**
    Refer to '[upload packages to PyPI]' for detailed instructions about the required procedures.

    Run the following command in your terminal:

    === ":octicons-zap-24: Invoke"

        ```bash linenums="0"
        invoke release
        ```

    === ":simple-uv: u"

        ```bash linenums="0"
        uv publish
        ```

    This will build and publish your package to PyPI. If you're publishing to a private repository, you can specify the repository with the `--publish-url` option, including the name of the private repository provided in the `pyproject.toml` file.

    ```bash linenums="0"
    uv publish --publish-url <name_of_private_repo>
    ```

7. **Verify the registration.**
    Visit [PyPI] to make sure your package is registered and visible.

## For Every Release

1. Update `HISTORY.md` file with the changes made for the new release.

2. Commit the changes

    Committing changes to your version control system is a crucial part of every release. It ensures that every change is tracked and can be reverted if necessary.

    The recommended option is to use [Commitizen]:

    ```bash linenums="0"
    git add .
    uv run cz commit
    ```

    When you run this command, Commitizen will prompt you to fill out a commit message in a specific format. This format typically includes the type of change (e.g., feature, bugfix), a short description, and optionally a longer description and any breaking changes.

    If you’re not using Commitizen, you can manually add and commit your changes with Git:

    ```bash linenums="0"
    git add .
    git commit -m "Changelog for upcoming release x.y.z"
    ```

    Remember, it’s important to write clear and descriptive commit messages that accurately represent your changes.

3. **Update version number**

    The version number of your package is a crucial piece of information that helps users and contributors understand the current state of your project. It’s important to update the version number whenever you make a significant change to your project. For more information see [SemVer].

    The recommended method for updating the version number is to use [Commitizen]:

    ```bash linenums="0"
    uv run cz bump
    ```

    When you run this command, Commitizen will bump your project’s version according to the changes that have been made since the last release. It determines the type of version bump (major, minor, or patch) based on the commit messages. This is why it’s important to follow a standard commit message format.

    The version can also be provided:

     ```bash linenums="0"
    uv run cz bump 0.1.0
    ```

    Commitizen will also update the version in several files accross the project. These files must be defined in the `version_files` list under the `[tool.commitizen]` section in `pyproject.toml`.

    ~~If you are not using Commitizen, you can manually update the version number using [uv] (the new version can be 'major', 'minor', or 'patch'):~~ # NOTE: not yet available for uv

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

    Alternatively, it is possible to run the pre-release check can be run, which will execute all the lint/formatting tools along with the tests in `test-all`:

    ```bash linenums="0"
        invoke pre-release-check
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

8. Check the PyPI listing

    After pushing your tags and triggering a new release, check the PyPI listing page to make sure that the README, release notes, and roadmap display properly. If not, try copying and pasting the Markdown into an online Markdown editor like Dillinger to find out what broke the formatting.

9. Edit the release on GitHub (e.g. <https://github.com/psolsfer/cookiecutter-pypackage-uv/releases>)

    Paste the release notes into the release's release page, and come up with a title for the release

## About This Checklist

This checklist is adapted from:

- <https://gist.github.com/audreyr/5990987>
- <https://gist.github.com/audreyr/9f1564ea049c14f682f4>
- <https://github.com/audreyfeldroy/cookiecutter-pypackage/blob/master/docs/pypi_release_checklist.rst>

[Commitizen]: http://commitizen.github.io/cz-cli/
[PyPI]: https://pypi.org/
[SemVer]: https://semver.org/
[upload packages to PyPI]: https://packaging.python.org/en/latest/tutorials/packaging-projects/#uploading-the-distribution-archives
[uv]: <https://docs.astral.sh/uv/>
