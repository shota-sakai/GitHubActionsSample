def lambda_handler(event, context):
    print("テスト")
    return {
        "statusCode": 200,
        "body": "Hello from Lambda!"
    }
