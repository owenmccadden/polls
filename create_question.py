import json
import boto3
from datetime import datetime
#That's the lambda handler, you can not modify this method
# the parameters from JSON body can be accessed like deviceId = event['deviceId']
def lambda_handler(event, context):
    # Instanciating connection objects with DynamoDB using boto3 dependency
    dynamodb = boto3.resource('dynamodb')
    client = boto3.client('dynamodb')
    
    # Getting the table the table questions object
    questions_table = dynamodb.Table('questions')
    
    # current datetime as a potential timestamp attribute
    # event_timestamp = (datetime.now()).strftime("%Y-%m-%d %H:%M:%S")
    question_id = event['question_id']
    question = event['question']
    responses = []
    
    # Putting a try/catch to log to user when some error occurs
    try:
        
        questions_table.put_item(
           Item={
                # 'event_timestamp': event_timestamp,
                'question_id': question_id,
                'question': question,
                'responses': responses
            }
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps('Succesfully inserted temperature!')
        }
    except:
        print('Closing lambda function')
        return {
                'statusCode': 400,
                'body': json.dumps('Error saving the temperature')
        }



