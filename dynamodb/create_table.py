import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

# Create the DynamoDB table.
login_table = dynamodb.create_table(
    TableName='login',
    KeySchema=[
        {
            'AttributeName': 'email',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'user_name',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'email',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'user_name',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

# Wait until the table exists.
login_table.wait_until_exists()

# Print out some data about the table.
print(login_table.item_count)
