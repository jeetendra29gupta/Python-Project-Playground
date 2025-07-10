import requests

# ==========================================
# 🔗 Step 1: Base API URL
# ==========================================
BASE_URL = "http://localhost:8181"


# ==========================================
# 🔁 Step 2: API Functions
# ==========================================

def reset_todos():
    """
    Calls the API endpoint to delete all todos,
    effectively resetting the todo list.

    Returns:
        dict: Response JSON with status message.
    """
    response = requests.delete(f"{BASE_URL}/reset/todos")
    response.raise_for_status()
    return response.json()


def create_todo(task: str):
    """
    Creates a new todo item.

    Args:
        task (str): Task description

    Returns:
        dict: Created todo item
    """
    response = requests.post(f"{BASE_URL}/todos", params={"task": task})
    response.raise_for_status()
    return response.json()


def get_all_todos():
    """
    Retrieves all todos from the API.

    Returns:
        list[dict]: List of todos
    """
    response = requests.get(f"{BASE_URL}/todos")
    response.raise_for_status()
    return response.json()


def get_todo_by_id(tid: int):
    """
    Retrieves a specific todo by ID.

    Args:
        tid (int): Todo ID

    Returns:
        dict: Todo item
    """
    response = requests.get(f"{BASE_URL}/todos/{tid}")
    response.raise_for_status()
    return response.json()


def update_todo(tid: int, task: str):
    """
    Updates the task description of a todo.

    Args:
        tid (int): Todo ID
        task (str): New task description

    Returns:
        dict: Updated todo item
    """
    response = requests.put(f"{BASE_URL}/todos/{tid}", params={"task": task})
    response.raise_for_status()
    return response.json()


def patch_todo_status(tid: int, is_done: bool):
    """
    Updates the status (done/pending) of a todo.

    Args:
        tid (int): Todo ID
        is_done (bool): Completion status

    Returns:
        dict: Updated todo item
    """
    response = requests.patch(f"{BASE_URL}/todos/{tid}", params={"is_done": str(is_done).lower()})
    response.raise_for_status()
    return response.json()


def delete_todo(tid: int):
    """
    Deletes a specific todo by ID.

    Args:
        tid (int): Todo ID

    Returns:
        str: Confirmation message
    """
    response = requests.delete(f"{BASE_URL}/todos/{tid}")
    response.raise_for_status()
    return response.text


# ==========================================
# 🚀 Step 3: Demo Script
# ==========================================

def main():
    print("=== 🔄 Resetting All Todos ===")
    reset_resp = reset_todos()
    print(reset_resp)

    tasks = [
        "Buy groceries",
        "Walk the dog",
        "Write FastAPI code",
        "Read a book",
        "Exercise for 30 minutes"
    ]

    created_todos = []

    print("\n=== 🆕 Creating Multiple Todos ===")
    for task in tasks:
        todo = create_todo(task)
        print(todo)
        created_todos.append(todo)

    # Extract ID of the first created todo
    first_todo_id = created_todos[0]["tid"]

    print("\n=== 📋 Getting All Todos ===")
    for todo in get_all_todos():
        print(todo)

    print("\n=== 🔍 Getting Todo by ID ===")
    print(get_todo_by_id(first_todo_id))

    print("\n=== ✏️ Updating Todo (PUT) ===")
    updated = update_todo(first_todo_id, "Buy groceries and cook dinner")
    print(updated)

    print("\n=== ✅ Patching Todo Status (PATCH) ===")
    patched = patch_todo_status(first_todo_id + 1, True)
    print(patched)

    print("\n=== ❌ Deleting a Todo ===")
    deleted = delete_todo(first_todo_id + 2)
    print(deleted)

    print("\n=== 📋 Todos After Deletion ===")
    for todo in get_all_todos():
        print(todo)


# ==========================================
# ▶️ Entry Point
# ==========================================

if __name__ == "__main__":
    main()
