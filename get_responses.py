import json
import boto3

def lambda_handler(event, context):
    # Instanciating connection objects with DynamoDB using boto3 dependency
    dynamodb = boto3.resource('dynamodb')
    
    # Getting the table the table questions object
    questions_table = dynamodb.Table('questions')
    
    question_id = event['question_id']
    
    # Putting a try/catch to log to user when some error occurs
    try:
        
        response = questions_table.get_item(
           Key={
               'question_id': question_id
           }
        )

        if response['Item'] is None:
            raise KeyError("Question_id {} does not exist in table.".format(event['question_id']))
        
        return {
            'statusCode': 200,
            'body': response['Item']['responses']
        }

    except Exception as e:
        print('Closing lambda function')
        return {
                'statusCode': 400,
                'body': json.dumps('Error getting responses. {}'.format(e))
        }
