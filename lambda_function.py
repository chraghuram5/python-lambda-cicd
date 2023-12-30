def lambda_handler(event, context):
    print("lambda triggered")
    print(event)
    return 'Hello from Lambda again and again!'
