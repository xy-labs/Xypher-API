import requests
import json

#Get all the liquidations above 100000 USD and above 30k price.
payload = {'key': '<YOUR-KEY>', 'market': 'BTCUSDT', 'above_amount': 100000, 'above_rate': 30000}
r = requests.get('http://api.xypher.io/v1/liquidations/', params=payload)

data = r.json()

liqs = [liq for liq in data['results']]
print(liqs)

