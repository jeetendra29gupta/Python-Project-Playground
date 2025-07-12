# 🔧 Master Poetry Example

A demonstration project showcasing how to build a Python application using **Poetry**, **Flask**, **Click**, automatic
formatting (**Black**), and **pytest** for testing.

---

## 🧩 Project Overview

Utilizing modern tools and best practices:

- **Poetry** – Dependency and package management
- **Flask** – Web application framework
- **Click** – CLI toolkit
- **Black** – Code formatting/ linting
- **pytest** – Automated testing

---

## ⚙️ Setup

### 1. Create Project

```bash
poetry new master_poetry_example
cd master_poetry_example
````

### 2. Add Dependencies

```bash
poetry add flask click
poetry add --group dev black pytest
```

---

## 🗃️ Project Structure

```
master_poetry_example/
├── pyproject.toml
├── README.md
├── src/
│   └── master_poetry_example/
│       ├── __init__.py
│       ├── client.py
│       └── server.py
└── tests/
    ├── __init__.py
    └── test_app.py
```

---

## 📝 `pyproject.toml` Highlights

Make sure to include proper configuration for scripts and formatting tools:

```toml
[project]
name = "master-poetry-example"
version = "0.1.0"
description = ""
authors = [
    { name = "Your Name", email = "you@example.com" }
]
readme = "README.md"
requires-python = ">=3.11"
dependencies = [
    "flask (>=3.1.1,<4.0.0)",
    "click (>=8.2.1,<9.0.0)"
]

[tool.poetry]
packages = [{ include = "master_poetry_example", from = "src" }]

[tool.poetry.scripts]
server = "master_poetry_example.server:main"
client = "master_poetry_example.client:main"


[tool.poetry.group.dev.dependencies]
black = "^25.1.0"
pytest = "^8.4.1"

[build-system]
requires = ["poetry-core>=2.0.0,<3.0.0"]
build-backend = "poetry.core.masonry.api"

```

---

## 🚀 Example Code

### `src/master_poetry_example/server.py`

```python
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello from Flask!"


def main():
    app.run(host="0.0.0.0", port=8181, debug=True)


if __name__ == "__main__":
    main()

```

### `src/master_poetry_example/client.py`

```python
import click


@click.command()
@click.option("--name", default="World", help="Name to greet")
def main(name: str):
    print(f"Hello, {name} from Click + Poetry!")

```

---

## 🔧 Run Commands

### ✅ Install and setup the venv

```bash
poetry install
```

### **Output:**
```text
Updating dependencies
Resolving dependencies... (1.7s)

Package operations: 16 installs, 0 updates, 0 removals

  - Installing markupsafe (3.0.2)
  - Installing blinker (1.9.0)
  - Installing click (8.2.1)
  - Installing iniconfig (2.1.0)
  - Installing itsdangerous (2.2.0)
  - Installing jinja2 (3.1.6)
  - Installing mypy-extensions (1.1.0)
  - Installing packaging (25.0)
  - Installing pathspec (0.12.1)
  - Installing platformdirs (4.3.8)
  - Installing pluggy (1.6.0)
  - Installing pygments (2.19.2)
  - Installing werkzeug (3.1.3)
  - Installing black (25.1.0)
  - Installing flask (3.1.1)
  - Installing pytest (8.4.1)

Writing lock file

Installing the current project: master-poetry-example (0.1.0)

```


### Launch web server

```bash
poetry run server
```

### **Output:**
```text
 * Serving Flask app 'master_poetry_example.server'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:8181
 * Running on http://192.168.18.44:8181
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 135-993-054
```

Visit `http://127.0.0.1:8181` to see **"Hello from Flask!"**.

### Use CLI tool

```bash
poetry run client --name Jeetendra
```
### **Output:**
```text
Hello, Jeetendra from Click + Poetry!
```

---

## 🧼 Code Formatting

Run formatters:

```bash
poetry run black src tests
```

### **Output:**
```text
All done! ✨ 🍰 ✨
5 files left unchanged.
```


---

## 🧪 Testing

Example test: `tests/test_app.py`

```python
import pytest
from src.master_poetry_example.server import app
from src.master_poetry_example.client import main as cli_main
from click.testing import CliRunner


def test_root():
    client = app.test_client()
    res = client.get("/")
    assert res.data == b"Hello from Flask!"


def test_click_cli():
    runner = CliRunner()
    result = runner.invoke(cli_main, ["--name", "Jeetendra"])
    assert result.exit_code == 0
    assert "Hello, Jeetendra from Click + Poetry!" in result.output


if __name__ == "__main__":
    pytest.main(["-v", __file__])

```

Execute all tests:

```bash
poetry run pytest
```
### **Output:**
```text
======================================================================================================= test session starts ========================================================================================================
platform linux -- Python 3.11.2, pytest-8.4.1, pluggy-1.6.0
rootdir: /home/jeetendra/Workspace/master_poetry_example
configfile: pyproject.toml
collected 2 items                                                                                                                                                                                                                  

tests/test_app.py ..                                                                                                                                                                                                         [100%]

======================================================================================================== 2 passed in 0.10s =========================================================================================================
```

---

Congratulations – you now have a full-fledged Poetry project with web, CLI, formatting, and tests all in place! 🎉
