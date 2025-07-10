
# 📝 FastAPI Todo API with Python Client

A simple RESTful Todo API built with **FastAPI** and **SQLite** using **SQLAlchemy ORM**, accompanied by a Python client to interact with the API via HTTP requests using the `requests` library.

---

## 🚀 Features

- ✅ Create, Read, Update, Delete (CRUD) todo items
- 📋 Mark tasks as done or pending
- 🔁 Reset all todos in the database
- 🧪 Testable Python client with real-time interaction
- 💾 SQLite-based lightweight backend

---

## 📂 Project Structure

```plaintext
.
├── main.py                # FastAPI server with CRUD routes
├── client.py              # Python client using requests to test the API
├── todo.db                # SQLite database (auto-generated)
└── README.md              # Project documentation
````

---

## ⚙️ Requirements

* Python 3.8+
* FastAPI
* Uvicorn
* SQLAlchemy
* Requests

### 📦 Install Dependencies

```bash
pip install fastapi uvicorn sqlalchemy requests
```

---

## ▶️ How to Run

### 1. Start the API Server

```bash
uvicorn main:app --reload --port 8181
```

* This will run the server at: [http://localhost:8181](http://localhost:8181)
* You can access interactive API docs at: [http://localhost:8181/docs](http://localhost:8181/docs)

---

### 2. Run the Python Client

In a separate terminal:

```bash
python client.py
```

This will:

* Reset the todo list
* Create several todos
* Fetch all todos
* Retrieve a specific todo by ID
* Update a todo task
* Patch its status
* Delete one of the todos
* Fetch the final list to confirm changes

---

## 📬 API Endpoints Summary

| Method | Endpoint          | Description                   |
| ------ | ----------------- | ----------------------------- |
| GET    | `/`               | Welcome message               |
| POST   | `/todos?task=...` | Create a new todo             |
| GET    | `/todos`          | List all todos                |
| GET    | `/todos/{tid}`    | Get a todo by ID              |
| PUT    | `/todos/{tid}`    | Update a todo's task          |
| PATCH  | `/todos/{tid}`    | Update a todo's status (done) |
| DELETE | `/todos/{tid}`    | Delete a specific todo        |
| DELETE | `/reset/todos`    | Delete all todos (reset DB)   |

---

## ✅ Sample Todo Object

```json
{
  "tid": 1,
  "task": "Buy groceries",
  "status": false
}
```

---

## 🧪 Testing Ideas

You can extend `client.py` or use `pytest` to automate:

* Status code checks
* Task and status value verification
* Full lifecycle test (create → update → patch → delete)

Let me know if you'd like a test version!

---

## 📌 Notes

* The database is reset each time you run the client (via `reset_todos()`).
* The app uses SQLite for simplicity; swap with PostgreSQL or MySQL easily if needed.
* FastAPI provides automatic OpenAPI docs for quick testing.

---