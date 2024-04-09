import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')


def check_login_details(input_email, input_password):

    try:
        login_table = dynamodb.Table('login')
        response = login_table.get_item(
            Key={
                'email': input_email,
            }
        )
        item = response['Item']
        if item['password'] == input_password:
            return True
        return False
    except Exception as e:
        print(e)
        return False

print(check_login_details('s39271980@student.rmit.edu.au', '012345'))