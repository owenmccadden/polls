import json
import boto3
def lambda_handler(event, context):
  # Instanciating connection objects with DynamoDB using boto3 dependency
    dynamodb = boto3.resource('dynamodb')
    client = boto3.client('dynamodb')
    
    # Getting the table the table questions object
    questions_table = dynamodb.Table('questions')
    
    # current datetime as a potential timestamp attribute
    question_id = event['question_id']
    response = [event['response']]
    
    # Putting a try/catch to log to user when some error occurs
    try:

        questions_table.update_item(
          Key={
               'question_id': int(question_id)
           },
           UpdateExpression="SET responses = list_append(responses, :response)",
           ExpressionAttributeValues={
            ':response': response,
          }
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps('Succesfully created response!')
        }
    except Exception as e:
        print('Closing lambda function')
        return {
                'statusCode': 400,
                'body': json.dumps('Error creating the response. {}'.format(e))
        }