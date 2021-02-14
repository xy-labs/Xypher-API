import requests
import json

#Get all the liquidations above 100000 USD and above 30k price.
payload = {'key': '<YOUR-KEY>', 'exchange': 'binance'}
r = requests.get('http://api.xypher.io/v1/markets/', params=payload)

data = r.json()

markets = [market for market in data['results']]
print(markets)

