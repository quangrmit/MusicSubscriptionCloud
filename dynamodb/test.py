import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')


def check_register_details(input_email, input_user_name, input_password):
    login_table = dynamodb.Table('login')

    response = login_table.get_item(
        Key={
            'email': input_email,
        
        }
    )
    if 'Item' not in response.keys():
        # put item in db
        login_table.put_item(Item={
            'email': input_email,
            'user_name': input_user_name,
            'password': input_password
        })
    else:
        # notify user of identical
        pass

check_register_details('s39271980@student.rmit.edu.vn', 'something', 'something')
