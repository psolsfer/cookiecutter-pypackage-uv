# Contributing

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

Look through the GitHub issues for bugs. Anything tagged with "bug" and "help wanted" is open to whoever wants to implement it.

### Implement Features

Look through the GitHub issues for features. Anything tagged with "enhancement" and "help wanted" is open to whoever wants to implement it.

### Write Documentation

Cookiecutter PyPackage uv could always use more documentation, whether as part of the official docs, in docstrings, or even on the web in blog posts, articles, and such.

### Submit Feedback

The best way to send feedback is to file an issue at [Issues].

If you are proposing a feature:

- Explain in detail how it would work.
- Keep the scope as narrow as possible, to make it easier to implement.
- Remember that this is a volunteer-driven project, and that contributions are welcome :)

### Get Started

Ready to contribute? Here's how to set up `cookiecutter-pypackage-uv` for local development.

1. Fork the `cookiecutter-pypackage-uv` repo on GitHub.
2. Clone your fork locally:

    ```bash linenums="0"
    git clone git@github.com:YOUR_NAME/cookiecutter-pypackage-uv.git
    ```

3. Set up your local copy with uv.

    First, navigate to your project directory:

    ```bash linenums="0"
    cd cookiecutter-pypackage-uv/
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

   Now you can make your changes locally.

5. When you're done making changes, check that your changes pass the tests, including testing other Python versions with tox:

    ```bash linenums="0"
    invoke test-all
    ```

6. Commit your changes and push your branch to GitHub:

    ```bash linenums="0"
    git add .
    git commit -m "Your detailed description of your changes."
    git push origin name-of-your-bugfix-or-feature
    ```

7. Submit a pull request through the GitHub website.

### Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.md.
3. The pull request should work for Python 3.10, and 3.11, and for PyPy. Check <https://github.com/psolsfer/cookiecutter-pypackage-uv> and make sure that the tests pass for all supported Python versions.

### Add a New Test

When fixing a bug or adding features, it's good practice to add a test to
demonstrate your fix or new feature behaves as expected. These tests should
focus on one tiny bit of functionality and prove changes are correct.

To write and run your new test, follow these steps:

1. Add the new test to `tests/test_bake_project.py`. Focus your test on the
   specific bug or a small part of the new feature.

2. If you have already made changes to the code, stash your changes and confirm
   all your changes were stashed:

   ```bash linenums="0"
    git stash
    git stash list
    ```

3. Run your test and confirm that your test fails. If your test does not fail,
   rewrite the test until it fails on the original code:

    ```bash linenums="0"
    uv run pytest ./tests
    ```

4. (Optional) Run the tests with tox to ensure that the code changes work with different Python versions:

    ```bash linenums="0"
    uv run tox
    ```

5. Proceed work on your bug fix or new feature or restore your changes. To
   restore your stashed changes and confirm their restoration:

    ```bash linenums="0"
    git stash pop
    git stash list
    ```

6. Rerun your test and confirm that your test passes. If it passes,
   congratulations!

[Issues]: <https://github.com/psolsfer/cookiecutter-pypackage-uv/issues>
