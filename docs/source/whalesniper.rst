

Whalesniper
==================

Get Whalesniper signals. Available exchanges: Binance, Bitmex, Binance Futures, Bittrex,


.. code-block:: python

    GET /v1/whalesniper/?key=<YOUR_KEY>

**PARAMETERS:**

+------------+------------+-----------+
| PARAMETER  | TYPE       | MANDATORY |
+============+============+===========+
| market     | String     |    NO     |
+------------+------------+-----------+
| start_date | INT        |    NO     |
+------------+------------+-----------+
| end_date   | INT        |    NO     |
+------------+------------+-----------+
| limit      | INT        |    NO     |
+------------+------------+-----------+
| pair       | String     |    NO     |
+------------+------------+-----------+
| coin       | String     |    NO     |
+------------+------------+-----------+
| exchange   | String     |    NO     |
+------------+------------+-----------+
| trend      | String     |    NO     |
+------------+------------+-----------+



**market:** query WhaleSniper signals for a specific market :code:`/v1/whalesniper/?key=<YOUR_KEY>&market=<MARKET>`.
THE ACCEPTED MARKET FORMAT IS COINPAIR: SO BTCUSDT, ETHUSDT, BNBUSDT and so on

**start_date:** get all the signals after a specif timestamp, an integer unix timestamp must be provided.
:code:`/v1/whalesniper/?key=<YOUR_KEY>&start_date=<MARKET>`.

**end_date:** get all the signals before a specif timestamp, an integer unix timestamp must be provided.
:code:`/v1/whalesniper/?key=<YOUR_KEY>&end_date=<MARKET>`.

**limit:** specify a number of records to get from the API.
:code:`/v1/whalesniper/?key=<YOUR_KEY>&limit=<LIMIT>`.

**pair:** get all the signals for a specific pair
:code:`/v1/whalesniper/?key=<YOUR_KEY>&pair=<MARKET>`.

**Coin:** get all the signals for a specific coin across all the possible pairs
:code:`/v1/whalesniper/?key=<YOUR_KEY>&coin=<MARKET>`.

**exchange:** get all the signals from a specific exchange. Huobi. :code:`/v1/whalesniper/?key=<YOUR_KEY>&exchange=<MARKET>`.

**trend:** get all the signals with a specific direction: trend or bull.
:code:`/v1/whalesniper/?key=<YOUR_KEY>&trend=<bear/bull>`.

**Example:** :code:`/v1/whalesniper/?key=<YOUR-KEY>&market=BTCUSDT&exchange=binance`.

.. code-block:: json
	{
	  "count": 127,
	  "next": "http://api.xypher.io/v1/whalesniper/?exchange=binance&key=<YOUR-KEY>&market=BTCUSDT&page=2",
	  "previous": null,
	  "results": [
	    {
	      "market": "BTCUSDT",
	      "pair": "USDT",
	      "coin": "BTC",
	      "exchange": "Binance",
	      "oldAsk": "39497.92",
	      "newAsk": "41971.71",
	      "oldBid": "39484.25",
	      "newBid": "41955.92",
	      "oldVol": "2847768300.27",
	      "newVol": "3163939815.24",
	      "volDiff": "11",
	      "amount": "316171514.97",
	      "oldUnix": "1612788200",
	      "newUnix": "1612788879",
	      "trend": "bull"
	    },
	    {
	      "market": "BTCUSDT",
	      "pair": "USDT",
	      "coin": "BTC",
	      "exchange": "Binance",
	      "oldAsk": "33695.39",
	      "newAsk": "36831.52",
	      "oldBid": "33695.38",
	      "newBid": "36821.91",
	      "oldVol": "4158620050.73",
	      "newVol": "4616238341.94",
	      "volDiff": "11",
	      "amount": "457618291.21",
	      "oldUnix": "1611910065",
	      "newUnix": "1611910930",
	      "trend": "bull"
	    }
	  ]
	}

**RESPONSE**

**Market:** name of the market.

**Pair:** base pair.

**Coin:** base currency.

**Exchange:** exchange where the alert was found.

**oldAsk:** ask price BEFORE the trading activity took place.

**newAsk:** ask price AFTER the trading activity took place.

**oldBid:** bid price BEFORE the trading activity took place.

**newBid:** bid price AFTER the trading activity took place.

**oldVol:** volume BEFORE the trading activity took place.

**newVol:** volume AFTER the trading activity took place.

**volDiff:** volume difference before and after the trading activity took place.

**amount:** amount of the unusual trading activity.

**newUnix:** unix timestamp.

**trend:** direction of the unusual activity. Can be bull, bear, or neutral.