import json
import requests
import boto3

def lambda_handler(event, context):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        'ids': 'bitcoin',
        'vs_currencies': 'usd'
    }

    response = requests.get(url, params=params)
    data = response.json()

    price = data['bitcoin']['usd']
    message = f"🪙 Current Bitcoin Price: ${price}"

    sns = boto3.client('sns')
    sns.publish(
        TopicArn='arn:aws:sns:ap-south-1:674696818594:cryptonotification',
        Subject='Crypto Price Alert 🚀',
        Message=message
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Price sent to email!')
    }