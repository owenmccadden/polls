import json
import boto3
def lambda_handler(event, context):
  
  dynamodb = boto3.resource('dynamodb')
  questions_table = dynamodb.Table('questions')
  question_id = event['question_id']
  # response = questions_table.get_item(Key={'question_id': 100})
  response = questions_table.scan()
  print(response['Items'])
  return {
    'statusCode': 200,
    'body': response['Items']
  }

lambda_handler({'question_id': 0}, 'context')