import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

def remove_song(input_email, input_title):
    try:
        table = dynamodb.Table('login')

        response = table.get_item(
            Key={
                'email': input_email
            }
        )
        item = response['Item']

        curr = item['subscribed']
        curr.remove(input_title)
        table.update_item(
            Key={
                'email': input_email
            },
            UpdateExpression='SET subscribed = :val1',
            ExpressionAttributeValues={
                ':val1': curr
            }
        )
        return True
    except:
        return False

remove_song('foo1', 'Creep')
