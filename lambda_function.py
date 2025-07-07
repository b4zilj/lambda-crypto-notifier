import json
import requests

def lambda_handler(event, context):
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        'vs_currency': 'usd',
        'order': 'market_cap_desc',
        'per_page': 15,
        'page': 1,
        'sparkline': 'false'
    }

    response = requests.get(url, params=params)
    data = response.json()

    result = []
    for coin in data:
        coin_info = {
            'name': coin['name'],
            'symbol': coin['symbol'].upper(),
            'price_usd': coin['current_price']
        }
        result.append(coin_info)

    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }