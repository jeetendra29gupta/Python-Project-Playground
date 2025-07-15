import json


def lambda_handler(event, context):
    http_method = event.get("httpMethod", "")

    if http_method == "GET":
        return {
            "statusCode": 200,
            "body": json.dumps("Hello from Lambda via GET!")
        }

    elif http_method == "POST":
        try:
            body = json.loads(event.get("body", "{}"))
            name = body.get("name", "Guest")
            return {
                "statusCode": 201,
                "body": json.dumps(f"Hello, {name} from Lambda via POST!")
            }
        except Exception as e:
            return {
                "statusCode": 400,
                "body": json.dumps(f"Error: {str(e)}")
            }

    else:
        return {
            "statusCode": 405,
            "body": json.dumps("Method Not Allowed")
        }
