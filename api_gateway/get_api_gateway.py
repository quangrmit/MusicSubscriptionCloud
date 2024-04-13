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
        items = search_music(title, year, artist)
        return items
    elif operation == "POST":
        # insert post operation
        pass

    else:
        return respond(ValueError('Unsupported method "{}"'.format(operation)))
