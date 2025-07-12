# 🎯 My Random Quote

A simple Python project that fetches a random quote from an external API using the `requests` library.
Managed and run using **Poetry** with a CLI command: `random_quote`.

---

## 🛠️ Project Setup

### 📁 Create the Project

```bash
poetry new my_random_quote
cd my_random_quote
```

This will generate the structure:

```
my_random_quote/
├── pyproject.toml
├── README.md
├── src/
│   └── my_random_quote/
│       └── __init__.py
└── tests/
    └── __init__.py
```

---

## ⚙️ Configuration

Edit the `pyproject.toml`:

```toml
[project]
name = "my-random-quote"
version = "0.1.0"
description = ""
authors = [{ name = "Your Name", email = "you@example.com" }]
readme = "README.md"
requires-python = ">=3.11"
dependencies = ["requests (>=2.32.4,<3.0.0)"]

[tool.poetry]
packages = [{ include = "my_random_quote", from = "src" }]

[tool.poetry.scripts]
random_quote = "my_random_quote.main:app"

[build-system]
requires = ["poetry-core>=2.0.0,<3.0.0"]
build-backend = "poetry.core.masonry.api"
```

---

## 📦 Poetry Check

```bash
poetry check
```

This command checks the `pyproject.toml` for any issues and ensures everything is set up correctly.

---

## 📦 Install Dependencies

```bash
poetry install
poetry add requests
```

---

## 🧠 Add the Quote Script

Create a file at `src/my_random_quote/main.py`:

```python
# src/my_random_quote/main.py
import requests


def app():
    response = requests.get('https://dummyjson.com/quotes/random')
    data = response.json()
    quote = data['quote']
    author = data['author']
    print(f'"{quote}" - By: {author}')


if __name__ == '__main__':
    app()
```

---

## 🚀 Run the CLI Script

Execute the script using Poetry:

```bash
poetry run random_quote
```

💬 Example Output:

```
"If You Can'T Make It Good, At Least Make It Look Good." - By: Bill Gates
```

---

## ✅ Poetry Environment Info

Check the virtual environment:

```bash
poetry env info
poetry env list
```

---

## 📂 Tests

> You can place your test files in the `tests/` directory (optional for now).

---

## 🧼 Clean Up or Rebuild

To delete and recreate the environment:

```bash
rm -rf .venv
poetry install
```

---

