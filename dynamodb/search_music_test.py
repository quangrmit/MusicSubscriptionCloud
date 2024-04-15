import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

def search_music(input_title=None, input_year=None, input_artist=None):

    table = dynamodb.Table('music')

    if input_title.strip() != '':
        if input_year.strip() != '' and input_artist.strip() != '':
            response = table.scan(
                FilterExpression=Attr('year').eq(input_year) & Attr('artist').eq(input_artist) & Key('title').eq(input_title)
            )
        elif input_year.strip() != '':
            response = table.scan(
                FilterExpression=Attr('year').eq(input_year) & Key('title').eq(input_title)
            )
        elif input_artist.strip() != '':
            response = table.scan(
                FilterExpression=Attr('artist').eq(input_artist) & Key('title').eq(input_title)
            )
        else:
            response = table.scan(
                FilterExpression=Key('title').eq(input_title)
            )
    elif input_year.strip() != '':

        if input_artist.strip() != '':
            response = table.scan(
                FilterExpression=Attr('year').eq(input_year) & Attr('artist').eq(input_artist)
            )
        else:
            response = table.scan(
                FilterExpression=Attr('year').eq(input_year)
            )
    elif input_artist.strip() != '':
        response = table.scan(
            FilterExpression=Attr('artist').eq(input_artist)
        )
    else:
        response = None

    if response:
        items = response['Items']

    return items

print(search_music(input_year='1981', input_artist='John Lennon', input_title='    '))
