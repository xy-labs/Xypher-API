import requests
import json

#Get how much Bitcoin moved against USDT in the latest 60 minutes.
payload = {'key': '<YOUR-KEY>', 'market': 'BTCUSDT', 'time': 60}
r = requests.get('http://api.xypher.io/v1/mm/', params=payload)

data = r.json()

print(data)