import boto3
from boto3.dynamodb.conditions import Key, Attr


def search_music(input_title=None, input_year=None, input_artist=None):

    client = boto3.resource('dynamodb')
    table = client.Table('music')

    if input_title.strip() != '':
        # Case 1: Title is provided
        if input_year.strip() != '' and input_artist.strip() != '':
            # Case 1.1: Title, year, and artist are provided
            response = table.scan(
                FilterExpression=Attr('year').eq(input_year) & Attr(
                    'artist').eq(input_artist) & Key('title').eq(input_title)
            )
        elif input_year.strip() != '':
            # Case 1.2: Title and year are provided
            response = table.scan(
                FilterExpression=Attr('year').eq(
                    input_year) & Key('title').eq(input_title)
            )
        elif input_artist.strip() != '':
            # Case 1.3: Title and artist are provided
            response = table.scan(
                FilterExpression=Attr('artist').eq(
                    input_artist) & Key('title').eq(input_title)
            )
        else:
            # Case 1.4: Only title is provided
            response = table.scan(
                FilterExpression=Key('title').eq(input_title)
            )
    elif input_year.strip() != '':
        # Case 2: Year is provided
        if input_artist.strip() != '':
            # Case 2.1: Year and artist are provided
            response = table.scan(
                FilterExpression=Attr('year').eq(
                    input_year) & Attr('artist').eq(input_artist)
            )
        else:
            # Case 2.2: Only year is provided
            response = table.scan(
                FilterExpression=Attr('year').eq(input_year)
            )
    elif input_artist.strip() != '':
        # Case 3: Artist is provided
        # Only artist is provided
        response = table.scan(
            FilterExpression=Attr('artist').eq(input_artist)
        )
    else:
        # Case 4: No input provided
        print("Please provide at least one input parameter.")
        response = None

    if response:
        items = response['Items']

    return items


def check_login_details(input_email, input_password):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    try:
        login_table = dynamodb.Table('login')
        response = login_table.get_item(
            Key={
                'email': input_email,
            }
        )
        item = response['Item']
        if item['password'] == input_password:
            return item['user_name']
        return False
    except Exception as e:
        print(e)
        return False


def lambda_handler(event, context):
    type = event['type']

    # this will create dynamodb resource object and
    # here dynamodb is resource name
    client = boto3.resource('dynamodb')

    # this will search for dynamoDB table
    # your table name may be different
    table = client.Table("music")

    if type == "get":
        title = event['title']
        year = event['year']
        artist = event['artist']
        items = search_music(
            input_title=title, input_year=year, input_artist=artist)

        resp = {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': '*'
            },
            'body': {
                'items': items
            }
        }

    elif type == "login":
        email = event['email']
        password = event['password']
        success = check_login_details(email, password)

        if success:
            resp = {
                'statusCode': 200,
                'headers': {
                    'Access-Control-Allow-Headers': 'Content-Type',
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Methods': '*'
                },
                'body': {
                    'login': success
                }
            }
        else:
            resp = {
                'statusCode': 200,
                'headers': {
                    'Access-Control-Allow-Headers': 'Content-Type',
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Methods': '*'
                },
                'body': {
                    'login': 'failed'
                }
            }

    elif type == "options":
        db_value = table.get_item(Key={'id': id})['Item']['Count']
        resp = {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': '*'
            },
            'body': {
                'Count': db_value
            }
        }
    else:

        db_value = table.get_item(Key={'id': id})['Item']['Count']
        table.put_item(Item={'id': id, 'Count':  db_value+1})
        new_value = table.get_item(Key={'id': id})['Item']['Count']

        resp = {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': '*'
            },
            'body': {
                'Count': new_value
            }
        }
    return resp
