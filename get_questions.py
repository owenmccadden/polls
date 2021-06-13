import json
import boto3
def lambda_handler(event, context):
  
  dynamodb = boto3.resource('dynamodb')
  questions_table = dynamodb.Table('questions')
  response = questions_table.scan()
  
  return {
    'statusCode': 200,
    'body': response
  }