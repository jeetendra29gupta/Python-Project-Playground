event = {}

if __name__ == '__main__':
    query_params = event.get("queryStringParameters") or {}
    print(query_params)

    path_params = event.get("pathParameters") or {}
    print(path_params)

    name_query = query_params.get("name")
    print(name_query)

    name_path = path_params.get("name")
    print(name_path)

    name = name_query or name_path or "Guest"
    path = event.get("path", "")
    response = f"Hello, {name} 👋! (Path: {path})"
    print(response)
