import requests

BASE_URL = "http://localhost:8181"


def reset_todos():
    """
    Calls the API endpoint to delete all todos,
    effectively resetting the todo list.

    Returns:
        Response JSON dict with status message.
    """
    response = requests.delete(f"{BASE_URL}/reset/todos")
    response.raise_for_status()
    return response.json()


def create_todo(task: str):
    """
    Creates a new todo task by calling the API.

    Args:
        task (str): The description of the todo task.

    Returns:
        Created todo item as a dict.
    """
    response = requests.post(f"{BASE_URL}/todos", params={"task": task})
    response.raise_for_status()
    return response.json()


def get_all_todos():
    """
    Fetches all todo tasks from the API.

    Returns:
        List of todos as dicts.
    """
    response = requests.get(f"{BASE_URL}/todos")
    response.raise_for_status()
    return response.json()


def get_todo_by_id(tid: int):
    """
    Fetches a single todo item by ID.

    Args:
        tid (int): Todo item ID.

    Returns:
        Todo item dict.
    """
    response = requests.get(f"{BASE_URL}/todos/{tid}")
    response.raise_for_status()
    return response.json()


def update_todo(tid: int, task: str):
    """
    Updates a todo's task description (PUT request).

    Args:
        tid (int): Todo item ID.
        task (str): New task description.

    Returns:
        Updated todo item dict.
    """
    response = requests.put(f"{BASE_URL}/todos/{tid}", params={"task": task})
    response.raise_for_status()
    return response.json()


def patch_todo_status(tid: int, is_done: bool):
    """
    Patches a todo's completion status.

    Args:
        tid (int): Todo item ID.
        is_done (bool): True if task is done, False otherwise.

    Returns:
        Updated todo item dict.
    """
    response = requests.patch(f"{BASE_URL}/todos/{tid}", params={"is_done": str(is_done).lower()})
    response.raise_for_status()
    return response.json()


def delete_todo(tid: int):
    """
    Deletes a todo by ID.

    Args:
        tid (int): Todo item ID.

    Returns:
        Response text or confirmation message.
    """
    response = requests.delete(f"{BASE_URL}/todos/{tid}")
    response.raise_for_status()
    return response.text


def main():
    print("=== Reset Todos ===")
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

    print("\n=== Create Multiple Todos ===")
    for task in tasks:
        todo = create_todo(task)
        print(todo)
        created_todos.append(todo)

    first_todo_id = created_todos[0]["tid"]

    print("\n=== Get All Todos ===")
    all_todos = get_all_todos()
    for todo in all_todos:
        print(todo)

    print("\n=== Get Todo by ID ===")
    single_todo = get_todo_by_id(first_todo_id)
    print(single_todo)

    print("\n=== Update Todo (PUT) ===")
    updated_todo = update_todo(first_todo_id, "Buy groceries and cook dinner")
    print(updated_todo)

    print("\n=== Patch Todo Status (PATCH) ===")
    patched_todo = patch_todo_status(first_todo_id + 1, True)
    print(patched_todo)

    print("\n=== Delete Todo ===")
    delete_msg = delete_todo(first_todo_id + 2)
    print(delete_msg)

    print("\n=== Get All Todos After Deletion ===")
    all_todos_after = get_all_todos()
    for todo in all_todos_after:
        print(todo)


if __name__ == "__main__":
    main()
