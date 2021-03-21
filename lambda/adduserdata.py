import json
import boto3
from botocore.exceptions import ClientError

dynamodb=boto3.resource('dynamodb')
table=dynamodb.Table('expdb')


def lambda_handler(event, context):
    # TODO implement
    print(event)
    userid=event['userid']
    month=event['month']
    income=event['income']
    rent=event['rent']
    utilities=event['utilities']
    food=event['food']
    insurance=event['insurance']
    results=event['results']
    savings=event['savings']
    if month=="january":
        try:
            response = table.update_item(
            Key={"userid": userid},
            UpdateExpression="set #attrName.income = :i, #attrName.savings=:s, #attrName.rent = :r, #attrName.utilities=:u, #attrName.food = :f, #attrName.insurance=:in, #attrName.results = :re",
            ExpressionAttributeNames = {
                "#attrName" : "January"
            },
            ExpressionAttributeValues={
                ':i': income,
                ':s': savings,
                ':r': rent,
                ':u': utilities,
                ':f': food,
                ':in': insurance,
                ':re': results
                
            },
            ReturnValues="UPDATED_NEW"
            )
            return response
        except ClientError as e:
            if e.response['Error']['Code'] == 'ValidationException':
                response = table.update_item(
                  Key={
                      "userid": userid
                  },
                  UpdateExpression="set #attrName = :attrValue",
                  ExpressionAttributeNames = {
                      "#attrName" : "January"
                  },
                  ExpressionAttributeValues={
                      ':attrValue': {
                            'income': income,
                            'rent': rent,
                            'utilities': utilities,
                            'food': food,
                            'income': insurance,
                            'results': results,
                            'savings': savings
                      }
                  },
                  ReturnValues="UPDATED_NEW"
              )
            else:
                raise  
        
        
    if month=="february":
        try:
            response = table.update_item(
            Key={"userid": userid},
            UpdateExpression="set #attrName.income = :i, #attrName.savings=:s, #attrName.rent = :r, #attrName.utilities=:u, #attrName.food = :f, #attrName.insurance=:in, #attrName.results = :re",
            ExpressionAttributeNames = {
                "#attrName" : "February"
            },
            ExpressionAttributeValues={
                ':i': income,
                ':s': savings,
                ':r': rent,
                ':u': utilities,
                ':f': food,
                ':in': insurance,
                ':re': results
                
            },
            ReturnValues="UPDATED_NEW"
            )
            return response
        except ClientError as e:
            if e.response['Error']['Code'] == 'ValidationException':
                response = table.update_item(
                  Key={
                      "userid": userid
                  },
                  UpdateExpression="set #attrName = :attrValue",
                  ExpressionAttributeNames = {
                      "#attrName" : "February"
                  },
                  ExpressionAttributeValues={
                      ':attrValue': {
                            'income': income,
                            'rent': rent,
                            'utilities': utilities,
                            'food': food,
                            'income': insurance,
                            'results': results,
                            'savings': savings
                      }
                  },
                  ReturnValues="UPDATED_NEW"
              )
            else:
                raise  
        
        
    if month=="march":
        try:
            response = table.update_item(
            Key={"userid": userid},
            UpdateExpression="set #attrName.income = :i, #attrName.savings=:s, #attrName.rent = :r, #attrName.utilities=:u, #attrName.food = :f, #attrName.insurance=:in, #attrName.results = :re",
            ExpressionAttributeNames = {
                "#attrName" : "March"
            },
            ExpressionAttributeValues={
                ':i': income,
                ':s': savings,
                ':r': rent,
                ':u': utilities,
                ':f': food,
                ':in': insurance,
                ':re': results
                
            },
            ReturnValues="UPDATED_NEW"
            )
            return response
        except ClientError as e:
            if e.response['Error']['Code'] == 'ValidationException':
                response = table.update_item(
                  Key={
                      "userid": userid
                  },
                  UpdateExpression="set #attrName = :attrValue",
                  ExpressionAttributeNames = {
                      "#attrName" : "March"
                  },
                  ExpressionAttributeValues={
                      ':attrValue': {
                            'income': income,
                            'rent': rent,
                            'utilities': utilities,
                            'food': food,
                            'income': insurance,
                            'results': results,
                            'savings': savings
                      }
                  },
                  ReturnValues="UPDATED_NEW"
              )
            else:
                raise  
        
        
    if month=="april":
        try:
            response = table.update_item(
            Key={"userid": userid},
            UpdateExpression="set #attrName.income = :i, #attrName.savings=:s, #attrName.rent = :r, #attrName.utilities=:u, #attrName.food = :f, #attrName.insurance=:in, #attrName.results = :re",
            ExpressionAttributeNames = {
                "#attrName" : "April"
            },
            ExpressionAttributeValues={
                ':i': income,
                ':s': savings,
                ':r': rent,
                ':u': utilities,
                ':f': food,
                ':in': insurance,
                ':re': results
                
            },
            ReturnValues="UPDATED_NEW"
            )
            return response
        except ClientError as e:
            if e.response['Error']['Code'] == 'ValidationException':
                response = table.update_item(
                  Key={
                      "userid": userid
                  },
                  UpdateExpression="set #attrName = :attrValue",
                  ExpressionAttributeNames = {
                      "#attrName" : "April"
                  },
                  ExpressionAttributeValues={
                      ':attrValue': {
                            'income': income,
                            'rent': rent,
                            'utilities': utilities,
                            'food': food,
                            'income': insurance,
                            'results': results,
                            'savings': savings
                      }
                  },
                  ReturnValues="UPDATED_NEW"
              )
            else:
                raise  
        
        
    if month=="may":
        try:
            response = table.update_item(
            Key={"userid": userid},
            UpdateExpression="set #attrName.income = :i, #attrName.savings=:s, #attrName.rent = :r, #attrName.utilities=:u, #attrName.food = :f, #attrName.insurance=:in, #attrName.results = :re",
            ExpressionAttributeNames = {
                "#attrName" : "May"
            },
            ExpressionAttributeValues={
                ':i': income,
                ':s': savings,
                ':r': rent,
                ':u': utilities,
                ':f': food,
                ':in': insurance,
                ':re': results
                
            },
            ReturnValues="UPDATED_NEW"
            )
            return response
        except ClientError as e:
            if e.response['Error']['Code'] == 'ValidationException':
                response = table.update_item(
                  Key={
                      "userid": userid
                  },
                  UpdateExpression="set #attrName = :attrValue",
                  ExpressionAttributeNames = {
                      "#attrName" : "May"
                  },
                  ExpressionAttributeValues={
                      ':attrValue': {
                            'income': income,
                            'rent': rent,
                            'utilities': utilities,
                            'food': food,
                            'income': insurance,
                            'results': results,
                            'savings': savings
                      }
                  },
                  ReturnValues="UPDATED_NEW"
              )
            else:
                raise  
        
        
    if month=="june":
        try:
            response = table.update_item(
            Key={"userid": userid},
            UpdateExpression="set #attrName.income = :i, #attrName.savings=:s, #attrName.rent = :r, #attrName.utilities=:u, #attrName.food = :f, #attrName.insurance=:in, #attrName.results = :re",
            ExpressionAttributeNames = {
                "#attrName" : "June"
            },
            ExpressionAttributeValues={
                ':i': income,
                ':s': savings,
                ':r': rent,
                ':u': utilities,
                ':f': food,
                ':in': insurance,
                ':re': results
                
            },
            ReturnValues="UPDATED_NEW"
            )
            return response
        except ClientError as e:
            if e.response['Error']['Code'] == 'ValidationException':
                response = table.update_item(
                  Key={
                      "userid": userid
                  },
                  UpdateExpression="set #attrName = :attrValue",
                  ExpressionAttributeNames = {
                      "#attrName" : "June"
                  },
                  ExpressionAttributeValues={
                      ':attrValue': {
                            'income': income,
                            'rent': rent,
                            'utilities': utilities,
                            'food': food,
                            'income': insurance,
                            'results': results,
                            'savings': savings
                      }
                  },
                  ReturnValues="UPDATED_NEW"
              )
            else:
                raise  
        
        
    if month=="july":
        try:
            response = table.update_item(
            Key={"userid": userid},
            UpdateExpression="set #attrName.income = :i, #attrName.savings=:s, #attrName.rent = :r, #attrName.utilities=:u, #attrName.food = :f, #attrName.insurance=:in, #attrName.results = :re",
            ExpressionAttributeNames = {
                "#attrName" : "July"
            },
            ExpressionAttributeValues={
                ':i': income,
                ':s': savings,
                ':r': rent,
                ':u': utilities,
                ':f': food,
                ':in': insurance,
                ':re': results
                
            },
            ReturnValues="UPDATED_NEW"
            )
            return response
        except ClientError as e:
            if e.response['Error']['Code'] == 'ValidationException':
                response = table.update_item(
                  Key={
                      "userid": userid
                  },
                  UpdateExpression="set #attrName = :attrValue",
                  ExpressionAttributeNames = {
                      "#attrName" : "July"
                  },
                  ExpressionAttributeValues={
                      ':attrValue': {
                            'income': income,
                            'rent': rent,
                            'utilities': utilities,
                            'food': food,
                            'income': insurance,
                            'results': results,
                            'savings': savings
                      }
                  },
                  ReturnValues="UPDATED_NEW"
              )
            else:
                raise  
        
        
    if month=="august":
        try:
            response = table.update_item(
            Key={"userid": userid},
            UpdateExpression="set #attrName.income = :i, #attrName.savings=:s, #attrName.rent = :r, #attrName.utilities=:u, #attrName.food = :f, #attrName.insurance=:in, #attrName.results = :re",
            ExpressionAttributeNames = {
                "#attrName" : "August"
            },
            ExpressionAttributeValues={
                ':i': income,
                ':s': savings,
                ':r': rent,
                ':u': utilities,
                ':f': food,
                ':in': insurance,
                ':re': results
                
            },
            ReturnValues="UPDATED_NEW"
            )
            return response
        except ClientError as e:
            if e.response['Error']['Code'] == 'ValidationException':
                response = table.update_item(
                  Key={
                      "userid": userid
                  },
                  UpdateExpression="set #attrName = :attrValue",
                  ExpressionAttributeNames = {
                      "#attrName" : "August"
                  },
                  ExpressionAttributeValues={
                      ':attrValue': {
                            'income': income,
                            'rent': rent,
                            'utilities': utilities,
                            'food': food,
                            'income': insurance,
                            'results': results,
                            'savings': savings
                      }
                  },
                  ReturnValues="UPDATED_NEW"
              )
            else:
                raise  
        
        
    if month=="september":
        try:
            response = table.update_item(
            Key={"userid": userid},
            UpdateExpression="set #attrName.income = :i, #attrName.savings=:s, #attrName.rent = :r, #attrName.utilities=:u, #attrName.food = :f, #attrName.insurance=:in, #attrName.results = :re",
            ExpressionAttributeNames = {
                "#attrName" : "September"
            },
            ExpressionAttributeValues={
                ':i': income,
                ':s': savings,
                ':r': rent,
                ':u': utilities,
                ':f': food,
                ':in': insurance,
                ':re': results
                
            },
            ReturnValues="UPDATED_NEW"
            )
            return response
        except ClientError as e:
            if e.response['Error']['Code'] == 'ValidationException':
                response = table.update_item(
                  Key={
                      "userid": userid
                  },
                  UpdateExpression="set #attrName = :attrValue",
                  ExpressionAttributeNames = {
                      "#attrName" : "September"
                  },
                  ExpressionAttributeValues={
                      ':attrValue': {
                            'income': income,
                            'rent': rent,
                            'utilities': utilities,
                            'food': food,
                            'income': insurance,
                            'results': results,
                            'savings': savings
                      }
                  },
                  ReturnValues="UPDATED_NEW"
              )
            else:
                raise  
        
        
    if month=="october":
        try:
            response = table.update_item(
            Key={"userid": userid},
            UpdateExpression="set #attrName.income = :i, #attrName.savings=:s, #attrName.rent = :r, #attrName.utilities=:u, #attrName.food = :f, #attrName.insurance=:in, #attrName.results = :re",
            ExpressionAttributeNames = {
                "#attrName" : "October"
            },
            ExpressionAttributeValues={
                ':i': income,
                ':s': savings,
                ':r': rent,
                ':u': utilities,
                ':f': food,
                ':in': insurance,
                ':re': results
                
            },
            ReturnValues="UPDATED_NEW"
            )
            return response
        except ClientError as e:
            if e.response['Error']['Code'] == 'ValidationException':
                response = table.update_item(
                  Key={
                      "userid": userid
                  },
                  UpdateExpression="set #attrName = :attrValue",
                  ExpressionAttributeNames = {
                      "#attrName" : "October"
                  },
                  ExpressionAttributeValues={
                      ':attrValue': {
                            'income': income,
                            'rent': rent,
                            'utilities': utilities,
                            'food': food,
                            'income': insurance,
                            'results': results,
                            'savings': savings
                      }
                  },
                  ReturnValues="UPDATED_NEW"
              )
            else:
                raise  
        
        
    if month=="november":
        try:
            response = table.update_item(
            Key={"userid": userid},
            UpdateExpression="set #attrName.income = :i, #attrName.savings=:s, #attrName.rent = :r, #attrName.utilities=:u, #attrName.food = :f, #attrName.insurance=:in, #attrName.results = :re",
            ExpressionAttributeNames = {
                "#attrName" : "November"
            },
            ExpressionAttributeValues={
                ':i': income,
                ':s': savings,
                ':r': rent,
                ':u': utilities,
                ':f': food,
                ':in': insurance,
                ':re': results
                
            },
            ReturnValues="UPDATED_NEW"
            )
            return response
        except ClientError as e:
            if e.response['Error']['Code'] == 'ValidationException':
                response = table.update_item(
                  Key={
                      "userid": userid
                  },
                  UpdateExpression="set #attrName = :attrValue",
                  ExpressionAttributeNames = {
                      "#attrName" : "November"
                  },
                  ExpressionAttributeValues={
                      ':attrValue': {
                            'income': income,
                            'rent': rent,
                            'utilities': utilities,
                            'food': food,
                            'income': insurance,
                            'results': results,
                            'savings': savings
                      }
                  },
                  ReturnValues="UPDATED_NEW"
              )
            else:
                raise  
        
        
    if month=="december":
        try:
            response = table.update_item(
            Key={"userid": userid},
            UpdateExpression="set #attrName.income = :i, #attrName.savings=:s, #attrName.rent = :r, #attrName.utilities=:u, #attrName.food = :f, #attrName.insurance=:in, #attrName.results = :re",
            ExpressionAttributeNames = {
                "#attrName" : "December"
            },
            ExpressionAttributeValues={
                ':i': income,
                ':s': savings,
                ':r': rent,
                ':u': utilities,
                ':f': food,
                ':in': insurance,
                ':re': results
                
            },
            ReturnValues="UPDATED_NEW"
            )
            return response
        except ClientError as e:
            if e.response['Error']['Code'] == 'ValidationException':
                response = table.update_item(
                  Key={
                      "userid": userid
                  },
                  UpdateExpression="set #attrName = :attrValue",
                  ExpressionAttributeNames = {
                      "#attrName" : "December"
                  },
                  ExpressionAttributeValues={
                      ':attrValue': {
                            'income': income,
                            'rent': rent,
                            'utilities': utilities,
                            'food': food,
                            'income': insurance,
                            'results': results,
                            'savings': savings
                      }
                  },
                  ReturnValues="UPDATED_NEW"
              )
            else:
                raise  
        
   
    
    """
    {
  "userid": "886898300202",
  "month": "july",
  "income": "25000",
  "rent": "6000",
  "utilities": "5000",
  "food": "2000",
  "insurance": "7000",
  "results": "2000",
  "savings": "5000"
}
    """
