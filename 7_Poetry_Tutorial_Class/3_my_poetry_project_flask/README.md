# My Poetry Project Flask

A simple Flask app managed with Poetry.

---

## 🛠️ Steps to Create Your Project

- Create a New Poetry Project
  First, let's create a new project folder with Poetry:

```bash
poetry new my_poetry_project_flask
cd my_poetry_project_flask
```

This will generate a basic project structure. For Flask, we’ll customize it slightly.

- Set up Poetry and Virtual Environment

```bash
poetry shell
```

- Install Flask as a Dependency

```bash
poetry add flask
```

- Create a Simple Flask App

```python
# src/my_poetry_project_flask/app.py
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, Poetry & Flask!'


if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')


```

- Run the Flask App

```bash
poetry run python src/my_poetry_project_flask/app.py
```

Visit http://127.0.0.1:5000 in your browser to see your app.

- Install Development Dependencies

```bash
poetry add --group dev pytest
```

This will add pytest to your dev group in pyproject.toml, so it’s only used during testing.

- Create Tests for Flask App

```python
# tests/test_app.py
import pytest

from src.my_poetry_project_flask.app import app


def test_hello_world():
    with app.test_client() as client:
        response = client.get('/')
        assert response.data == b'Hello, Poetry & Flask!'


if __name__ == '__main__':
    pytest.main()
```

- Run Tests with pytest

```bash
poetry run pytest
```

---

## 💡 Notes

- Your Flask app is running in a Poetry-managed virtual environment.
- Development dependencies (e.g., pytest) are included in the dev group of the pyproject.toml.

---

## 🚀 You’re Ready to Go!

You now have:

1. A **Flask app** with **Poetry** for dependency management.
2. **Basic testing** set up with **pytest**.
3. A solid **project structure** for Flask development.

---