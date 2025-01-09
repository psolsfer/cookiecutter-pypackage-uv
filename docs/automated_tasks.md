# Automated tasks

----

The generated project is ready to run some useful tasks like formatting, linting, testing. This is done using [Invoke](https://www.pyinvoke.org/) to wrap up the required commands.

you can see a list of all the available automations defined in the `tasks.py` file by running:

```bash linenums="0"
invoke --list
```

## Understanding available tasks

Each of the tasks can be run using the invoke command followed by the task name. For example, to run the format task, you would use:

```bash linenums="0"
invoke <task-name>
```

Here’s a brief overview of some of the tasks included in this project:

`lint`: This task checks your code for any issues or deviations from our style guidelines. It can be used with the `check=False` argument to automatically format the code and correct some of the issues found.

`test-all`: This task runs all tests in the project to ensure that everything is working as expected.

`pre_release_check`: This task agrupates the `lint` and `test-all` tasks.

`docs`: This task generates the project documentation with `mkdocs`.
