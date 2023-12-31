def lambda_handler(event, context):
    print("lambda triggggered")
    print(event)
    return 'Hello from Lambda again and again'
