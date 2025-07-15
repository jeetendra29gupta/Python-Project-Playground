import json


def lambda_handler(event, context):
    http_method = event['requestContext']['http']['method']
    if http_method == "GET":
        return {
            'statusCode': 200,
            'body': json.dumps('Hello from Lambda Function!')
        }
    elif http_method == "POST":
        http_body = event['body']
        body = json.loads(http_body)
        return {
            'statusCode': 201,
            'body': json.dumps({
                'message': 'Hello from Lambda Function POST!',
                'KEY 1': body['key1'],
                'KEY 2': body['key2'],
                'KEY 3': body['key3']
            })
        }
    else:
        return {
            'statusCode': 405,
            'body': json.dumps({
                "error": "method not allowed error code"
            })
        }
