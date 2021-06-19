import json
import boto3
def lambda_handler(event, context):
  # Instanciating connection objects with DynamoDB using boto3 dependency
    dynamodb = boto3.resource('dynamodb')
    client = boto3.client('dynamodb')
    
    # Getting the table the table questions object
    questions_table = dynamodb.Table('questions')
    
    # current datetime as a potential timestamp attribute
    # event_timestamp = (datetime.now()).strftime("%Y-%m-%d %H:%M:%S")
    question_id = event['question_id']
    response = event['response']
    
    # Putting a try/catch to log to user when some error occurs
    try:

        # question = questions_table.get_item(
        #     Key={
        #        'question_id': question_id
        #     }
        # )

        # response_id = len(question['Item']['responses']) + 1
        
        # question['Item']['responses'].append(
        #   {
        #     "response_id": response_id,
        #     "response": response
        #   }
        # )

        question = questions_table.get_item(
          Key={
            "question_id": question_id
          }
        )

        questions_table.update_item(
          Key={
               'question_id': question_id
           },
           UpdateExpression="SET responses = list_append(responses, :response)",
           ExpressionAttributeValues={
            ':response': existing_responses,
          }
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps('Succesfully created response!')
        }
    except:
        print('Closing lambda function')
        return {
                'statusCode': 400,
                'body': json.dumps('Error saving the question')
        }
