import requests
import json

#Get the latest Whalesniper signals for the BTC-USDT market
payload = {'key': '<YOUR-KEY>', 'market': 'BTCUSDT'}
r = requests.get('http://api.xypher.io/v1/whalesniper/', params=payload)

data = r.json()

signals = [signal for signal in data['results']]
print(signals)