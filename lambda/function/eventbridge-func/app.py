def lambda_handler(event, context):
    print("Eventbridgeテスト")
    return {
        "statusCode": 200,
        "body": "Hello from Lambda!"
    }
