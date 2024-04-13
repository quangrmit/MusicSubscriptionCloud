import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')


def subscribe(user_email, song_title):
    try: 
        table = dynamodb.Table('login')

        response = table.get_item(
            Key={
                'email': user_email
            }
        )
        item = response['Item']


        if 'subscribed' not in item:
            print("no songs")

            table.update_item(
                Key={
                    'email': user_email
                },
                UpdateExpression='SET subscribed = :val1',
                ExpressionAttributeValues={
                    ':val1': {song_title}
                }
            )
        else:
            curr = item['subscribed']
            curr.add(song_title)
            table.update_item(
                Key={
                    'email': user_email
                },
                UpdateExpression='SET subscribed = :val1',
                ExpressionAttributeValues={
                    ':val1': curr
                }
            )
        return True
    except: 
        return False

