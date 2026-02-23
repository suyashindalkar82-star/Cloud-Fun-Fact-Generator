import boto3
import random
import json

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("CloudFacts")

def lambda_handler(event, context):
    response = table.scan()
    items = response.get("Items", [])

    if not items:
        return {
            "statusCode": 500,
            "headers": {
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({"error": "No facts found"})
        }

    fact = random.choice(items)["FactText"]

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET,OPTIONS",
            "Access-Control-Allow-Headers": "*"
        },
        "body": json.dumps({"fact": fact})
    }
