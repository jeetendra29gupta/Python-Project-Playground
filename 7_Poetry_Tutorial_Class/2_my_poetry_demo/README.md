# 📦 My Poetry Demo

This is a demo project showcasing how to **initialize and manage a pre-existing Python project
using [Poetry](https://python-poetry.org/)** — the modern Python dependency and packaging manager.

---

## 🧰 Prerequisites

- Python 3.8 or higher
- Poetry installed

---

## 🚀 Project Setup Steps

### 1. 📁 Create Project Directory

```bash
mkdir my-poetry-demo
cd my-poetry-demo
```

---

### 2. 🛠️ Initialize Poetry for an Existing Project

```bash
poetry init
```

You will be prompted to fill out some metadata:

* Package name: `my-poetry-demo`
* Description: `Initialising a pre-existing project using POETRY`
* Author: `Jeetendra Gupta`
* Python version: `3.11`
* Dependencies: (leave blank or add interactively)
* Dev dependencies: (choose `no`)

---

### 3. 🗂️ Create Project Structure

```bash
mkdir src src/my_module tests
```

Then create your script inside `src/my_module`:

```python
# src/scripy.py

if __name__ == '__main__':
    print("This is a script that can be run directly.")
    print("Hello, world! This is 'My Poetry Demo script'.")
    print("Initialising a pre-existing project using POETRY.")
```

---

### 4. 📝 Create a `README.md` File

Poetry expects the `readme` file if it is referenced in `pyproject.toml`:

```bash
touch README.md
```

You can add any content (this file itself can be the README).

---

# 5. ✅ Install Dependencies

Install dependencies and create the virtual environment:

```bash
poetry install
```

### 6. 🐍 Run Your Python Script

Use Poetry to run the Python script inside the virtual environment:

```bash
poetry run python -m my_module.scrip
```

**Output:**

```
This is a script that can be run directly.
Hello, world! This is 'My Poetry Demo script'.
Initialising a pre-existing project using POETRY.
```

---

## 🧪 Next Steps

You can now begin adding:

* 📦 Dependencies using `poetry add`
* 🧪 Tests in the `tests/` directory
* 📂 Proper module/package layout under `src/`

---

Happy hacking with Poetry! 🐍✨

---