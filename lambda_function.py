def lambda_handler(event, context):
    print(event)
    return 'Hello from Lambda!'

def test(a,b):
    return a+b
print(test(2,3));
