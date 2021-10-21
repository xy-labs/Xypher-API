Examples
================================

**Get the latest signals for the BTCUSDT market across multiple exchanges**

.. code-block:: python

	import requests
	import json

	#Get the latest Whalesniper signals for the BTC-USDT market
	payload = {'key': '<YOUR-KEY>', 'market': 'BTCUSDT'}
	r = requests.get('http://api.xypher.io/v1/whalesniper/', params=payload)

	data = r.json()

	signals = [signal for signal in data['results']]
	print(signals)

	    


**Get all the walls above 300 BTC across the most popular exchanges**

.. code-block:: python

	import requests
	import json

	#Get all the walls across the most popular exchanges above 300 BTC
	payload = {'key': '<YOUR-KEY>', 'market': 'BTCUSDT', 'exchange': 'combined', 'timeframe': '30m', 'above_amount': 300}
	r = requests.get('http://api.xypher.io/v1/hmc/', params=payload)

	data = r.json()

	walls = [wall for wall in data['results']]
	print(walls)



	    

**Get all the liquidations above 100000 USD and above 30000 price for the BTCUSDT market**

.. code-block:: python

	import requests
	import json

	#Get all the liquidations above 100000 USD and above 30k price.
	payload = {'key': '<YOUR-KEY>', 'market': 'BTCUSDT', 'above_amount': 100000, 'above_rate': 30000}
	r = requests.get('http://api.xypher.io/v1/liquidations/', params=payload)

	data = r.json()

	liqs = [liq for liq in data['results']]
	print(liqs)


**Get a summary of all the markets on Binance**

.. code-block:: python

	import requests
	import json

	#Get all the liquidations above 100000 USD and above 30k price.
	payload = {'key': '<YOUR-KEY>', 'exchange': 'binance'}
	r = requests.get('http://api.xypher.io/v1/markets/', params=payload)

	data = r.json()

	markets = [market for market in data['results']]
	print(markets)

**Get how much Bitcoin moved against USDT in the latest 60 minutes**

.. code-block:: python

	import requests
	import json

	#Get how much Bitcoin moved against USDT in the latest 60 minutes.
	payload = {'key': '<YOUR-KEY>', 'market': 'BTCUSDT', 'time': 60}
	r = requests.get('http://api.xypher.io/v1/mm/', params=payload)

	data = r.json()

	print(data)

