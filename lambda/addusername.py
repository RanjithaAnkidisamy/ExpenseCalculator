import json
import boto3
dynamodb=boto3.resource('dynamodb')
table=dynamodb.Table('expdb')

def lambda_handler(event, context):
    # TODO implement
    print(event)
    userid=event['userid']
    mail=event['mail']
    response=table.update_item(
    Key={'userid':userid},
    UpdateExpression="set mail= :m",
    ExpressionAttributeValues={
        ':m':mail
        
    },
    ReturnValues="UPDATED_NEW")
    return response
    
    
    
"""
Test event
{
  "userid": "8723hshgsv27871",
  "mail": "abc@gmail.com"
}
"""
