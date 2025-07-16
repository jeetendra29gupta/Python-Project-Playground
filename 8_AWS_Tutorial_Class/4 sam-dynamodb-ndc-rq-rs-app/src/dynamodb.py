import os

import boto3


def get_dynamodb_table():
    """
    Initializes and returns a boto3 DynamoDB Table object.
    """
    table_name = os.environ.get("TABLE_NAME", "MyTable")
    dynamodb_endpoint = "http://192.168.18.44:8000"
    dynamodb = boto3.resource("dynamodb", endpoint_url=dynamodb_endpoint)
    table = dynamodb.Table(table_name)
    return table
