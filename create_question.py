import json
import boto3

def lambda_handler(event, context):
    # Instanciating connection objects with DynamoDB using boto3 dependency
    dynamodb = boto3.resource('dynamodb')
    client = boto3.client('dynamodb')
    
    # Getting the table the table Temperatures object
    questions_table = dynamodb.Table('questions')
    
    # Getting the current datetime and transforming it to string in the format bellow
    question_id = len(questions_table.scan()['Items'])
    question = event['question']
    responses = []
    
    # Putting a try/catch to log to user when some error occurs
    try:
        print(question_id)
        questions_table.put_item(
           Item={
                'question_id': question_id,
                'question': question,
                'responses': responses
            }
        )
        print(question_id)
        
        return {
            'statusCode': 200,
            'body': json.dumps('Succesfully inserted question!')
        }
    except:
        print('Closing lambda function')
        return {
                'statusCode': 400,
                'body': json.dumps('Error saving the question')
        }

lambda_handler({'question': "what's up?"}, "context")