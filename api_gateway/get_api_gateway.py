import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

def search_music(input_title=None, input_year=None, input_artist=None):

    table = dynamodb.Table('music')


    if input_title.strip() != '':
        # Case 1: Title is provided
        if input_year.strip() != '' and input_artist.strip() != '':
            # Case 1.1: Title, year, and artist are provided
            response = table.scan(
                FilterExpression=Attr('year').eq(input_year) & Attr('artist').eq(input_artist) & Key('title').eq(input_title)
            )
        elif input_year.strip() != '':
            # Case 1.2: Title and year are provided
            response = table.scan(
                FilterExpression=Attr('year').eq(input_year) & Key('title').eq(input_title)
            )
        elif input_artist.strip() != '':
            # Case 1.3: Title and artist are provided
            response = table.scan(
                FilterExpression=Attr('artist').eq(input_artist) & Key('title').eq(input_title)
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
                FilterExpression=Attr('year').eq(input_year) & Attr('artist').eq(input_artist)
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

    return []


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
        return True
    else:
        # notify user of identical
        return False
    
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
            return [item['email'], item['user_name']]
        return False
    except Exception as e:
        print(e)
        return False
    
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
        new_response = table.get_item(
            Key={
                'email': user_email
            }
        )
        new_item = new_response['Item']
        return list(new_item['subscribed'])
    except: 
        return False

def lambda_handler(event, context):
    '''Demonstrates a simple HTTP endpoint using API Gateway. You have full
    access to the request and response payload, including headers and
    status code.

    To scan a DynamoDB table, make a GET request with the TableName as a
    query string parameter. To put, update, or delete an item, make a POST,
    PUT, or DELETE request respectively, passing in the payload to the
    DynamoDB API as a JSON body.
    '''
    #print("Received event: " + json.dumps(event, indent=2))

    # return event
    operation = event['httpMethod']
    if operation == "GET":
        if 'email' in event['params']['querystring']:
            email = event['params']['querystring']['email']
            table = dynamodb.Table('login')
            response = table.get_item(
                Key={
                    'email': email
                }
            )
            item = response['Item']
            if 'subscribed' not in item:
                return []
            return list(item['subscribed'])
        else:
            try:
                artist = event['params']['querystring']['artist']
            except KeyError:
                artist = ''
            try:
                title = event['params']['querystring']['title']
            except KeyError:
                title = ''
            try:
                year = event['params']['querystring']['year']
            except KeyError:
                year = ''
            res_items = search_music(title, year, artist)
            return res_items
    elif operation == "POST":
        action = event['action']

        if action == 'register':
            email = event['email']
            username = event['username']
            password = event['password']

            if check_register_details(email, username, password):
                return "success"
            return "failed"
        

        elif action == 'login': 
            email = event['email']
            password = event['password']
            if check_login_details(email, password):
                return check_login_details(email, password)
            return 'failed'
        
        elif action == 'subscribe':
            email = event['email']
            title = event['title']

            if subscribe(email, title):
                return subscribe(email, title)        
            else:
                return False

    else:
        return respond(ValueError('Unsupported method "{}"'.format(operation)))
