import json
import boto3

def lambda_handler(event, context):
  
    dynamodb = boto3.resource('dynamodb')
    questions_table = dynamodb.Table('questions')
 
    try:
        response = questions_table.scan()
      
        return {
            'statusCode': 200,
            'body': response['Items']
        }
    except Exception as e:
        print("Error. Closing lambda function.")
        return {
            'statusCode': 400,
            'body': json.dumps('Error getting questions. {}'.format(e))
        }