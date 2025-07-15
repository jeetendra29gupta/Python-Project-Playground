import json


def lambda_handler(event, context):
    path = event.get("path", "")
    http_method = event.get("httpMethod", "")
    response = ""

    if http_method == "GET":
        # If using /greet?name=xyz
        query_params = event.get("queryStringParameters") or {}
        name_query = query_params.get("name")

        # If using /greet/xyz
        path_params = event.get("pathParameters") or {}
        name_path = path_params.get("name")

        name = name_query or name_path or "Guest"
        response = f"Hello, {name} 👋! (Path: {path})"

    return {
        "statusCode": 200,
        "body": json.dumps(response)
    }
