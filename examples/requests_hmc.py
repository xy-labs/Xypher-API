import requests
import json

#Get all the walls across the most popular exchanges above 300 BTC
payload = {'key': '<YOUR-KEY>', 'market': 'BTCUSDT', 'exchange': 'combined', 'timeframe': '30m', 'above_amount': 300}
r = requests.get('http://api.xypher.io/v1/hmc/', params=payload)

data = r.json()

walls = [wall for wall in data['results']]
print(walls)

