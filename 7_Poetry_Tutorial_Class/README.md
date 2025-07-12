# 🐍 Poetry - Python Dependency Management & Packaging

Poetry is a tool for dependency management and packaging in Python. It simplifies the process of creating and managing
Python projects, adding/removing packages, handling virtual environments automatically, and publishing packages to PyPI.

---

## 🔧 Getting Started with Poetry

### ✅ Install Poetry

You can easily install Poetry by running the following command:

```bash
  curl -sSL https://install.python-poetry.org | python3 -
````

After installation, ensure Poetry is in your path by adding the following to your `.bashrc` file:

```bash
  echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
  source ~/.bashrc
```

Verify the installation:

```bash
  poetry --version
```

---

# My Project

This project was created and is managed using **Poetry**, a Python dependency management and packaging tool.

---

## 📦 Create a New Project

To create a new project with Poetry, run:

```bash
  poetry new my_project
  cd my_project
```

This will create the following structure for your project:

```
my_project/
├── my_project/
│   └── __init__.py
├── tests/
│   └── __init__.py
├── pyproject.toml
└── README.md
```

---

## 🖥️ Install Poetry Shell Plugin

To enable the `poetry shell` command, install the Poetry shell plugin:

```bash
  poetry self add poetry-plugin-shell
```

### 🎮 Activate the Poetry Virtual Environment

To activate the Poetry virtual environment shell, use the following command:

```bash
  poetry shell
```

---

## 🛠️ Add & Remove Dependencies

### Add a Dependency

To add a package to your project, run:

```bash
  poetry add requests
```

This will add the `requests` package to your project and update your `pyproject.toml` file.

To add development dependencies (e.g., testing libraries):

```bash
  poetry add --group dev pytest
```

### Remove a Dependency

To remove a package, use:

```bash
  poetry remove requests
```

To remove a dev-only package:

```bash
  poetry remove --group dev pytest
```

This will update your `pyproject.toml` and `poetry.lock` file.

The poetry.lock file ensures that your project always installs the exact versions of dependencies that you’ve tested,
even if those dependencies update in the future.

---

## ⚡ Running Python Scripts Inside Poetry Environment

You can create and edit Python scripts inside the `src/my_project/` directory. For example:

```python
    # src/my_project/script.py
print("Hello World")
```

To run the script using Poetry’s virtual environment:

```bash
  poetry run python src/my_project/script.py
```

---

## 🚪 Deactivate the Virtual Environment

To exit the Poetry virtual environment shell:

```bash
  exit
```

---

Now you’re all set up to start managing your Python project with Poetry! 🎉

---

# Poetry Command Reference

A quick reference guide for using [Poetry](https://python-poetry.org/), a dependency management and packaging tool for
Python.

| Command                       | Description                                                                                                                                                                                |
|-------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `$ poetry --version`          | Displays the current installed version of Poetry. Useful for verifying the installation or checking compatibility.                                                                         |
| `$ poetry new <project-name>` | Creates a new Poetry project with the given name. It sets up a standard Python project structure including `pyproject.toml`.                                                               |
| `$ poetry init`               | Adds Poetry to an existing project. It walks you through creating a `pyproject.toml` file interactively.                                                                                   |
| `$ poetry run <command>`      | Executes a given command inside the virtual environment managed by Poetry. Useful for running scripts or applications using dependencies.                                                  |
| `$ poetry add <package>`      | Adds a dependency to your project by updating the `pyproject.toml` and installing the package. You can also specify version constraints.                                                   |
| `$ poetry update`             | Updates all dependencies specified in `pyproject.toml` to the latest allowed versions and updates `poetry.lock`.                                                                           |
| `$ poetry install`            | Installs all the dependencies listed in the `poetry.lock` file. If `poetry.lock` does not exist, it will be created.                                                                       |
| `$ poetry show`               | Displays a list of installed packages, their versions, and available updates. Use `--tree` to show dependency trees.                                                                       |
| `$ poetry lock`               | Resolves and pins the latest allowed versions of dependencies based on constraints in `pyproject.toml`, and updates `poetry.lock`.                                                         |
| `$ poetry lock --no-update`   | Refreshes the `poetry.lock` file without changing the versions of dependencies. Useful when switching environments.                                                                        |
| `$ poetry check`              | Validates the format and contents of your `pyproject.toml` file to ensure it’s correctly structured.                                                                                       |
| `$ poetry config --list`      | Lists the current Poetry configuration settings, including cache paths and virtual environment preferences.                                                                                |
| `$ poetry env list`           | Shows a list of virtual environments that Poetry has created or is managing for the current project.                                                                                       |
| `$ poetry export`             | Exports the locked dependencies from `poetry.lock` to other formats, such as `requirements.txt`, using `--format requirements.txt`. Useful for deploying to environments not using Poetry. |

---

## 📺 Video Tutorial

[Master Dependency Management with Poetry in Python | Full Beginner's Tutorial (2025)](https://www.youtube.com/watch?v=ZyDvBfiiFVM&t=672s)

[How to Create and Use Virtual Environments in Python With Poetry](https://www.youtube.com/watch?v=0f3moPe_bhk&t=505s)

---