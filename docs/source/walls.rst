Walls
==================

Get orderbook walls data. Available exchanges: Binance, Combined (FTX + Binance + Binance Futures + Bitmex)



.. code-block:: python

    GET /v1/hmc/?key=<YOUR_KEY>

**PARAMETERS:**

+------------+------------+-----------+
| PARAMETER  | TYPE       | MANDATORY |
+============+============+===========+
| market     | String     |    YES    |
+------------+------------+-----------+
| exchange   | String     |    YES    |
+------------+------------+-----------+
| timeframe  | String     |    YES    |
+------------+------------+-----------+
| start_date | INT        |    NO     |
+------------+------------+-----------+
| end_date   | INT        |    NO     |
+------------+------------+-----------+
|above_amount| Float      |    NO     |
+------------+------------+-----------+
|below_amount| Float      |    NO     |
+------------+------------+-----------+
|above_price | Float      |    NO     |
+------------+------------+-----------+
|below_price | Float      |    NO     |
+------------+------------+-----------+


**market (MANDATORY):** Get walls for a specific market :code:`/v1/hmc/?key=<YOUR_KEY>&market=<MARKET>`.
THE ACCEPTED MARKET FORMAT IS COINPAIR: SO BTCUSDT, ETHUSDT, BNBUSDT and so on

**exchange (MANDATORY):** Choose an exchange. :code:`/v1/hmc/?key=<YOUR_KEY>&exchange=<EXCHANGE>`.

**timeframe (MANDATORY):** Choose a timeframe. Available timeframes: 5m, 30m. :code:`/v1/hmc/?key=<YOUR_KEY>&timeframe=<TIMEFRAME>`.


**start_date:** Get all the data after a specif timestamp, an integer unix timestamp must be provided.
:code:`/v1/hmc/?key=<YOUR_KEY>&start_date=<MARKET>`.

**end_date:** Get all the data before a specif timestamp, an integer unix timestamp must be provided.
:code:`/v1/hmc/?key=<YOUR_KEY>&end_date=<MARKET>`.

**above_amount:** Get all liquidations above a specified amount. :code:`/v1/hmc/?key=<YOUR_KEY>&above_amount=<AMOUNT>`.

**below_amount:** Get all liquidations above a specified amount. :code:`/v1/hmc/?key=<YOUR_KEY>&below_amount=<AMOUNT>`.

**above_price:** Get all liquidations above a specified price. :code:`/v1/hmc/?key=<YOUR_KEY>&above_price=<PRICE>`.

**below_price:** Get all liquidations below a specified price. :code:`/v1/hmc/?key=<YOUR_KEY>&below_price=<PRICE>`.

**Example:** :code:`/v1/hmc/?key=<YOUR-KEY>&market=BTCUSDT&exchange=binance&timeframe=30m`.

.. code-block:: json

	{
	  "count": 66713,
	  "next": "http://51.79.25.135/v1/hmc/?exchange=binance&key=<YOUR-KEY>&market=BTCUSDT&page=2&timeframe=30m",
	  "previous": null,
	  "results": [
	    {
	      "UTCunix": 1605025800,
	      "price": 15500,
	      "amount": 257.00074,
	      "candle": "2020-11-10T16:30:00Z",
	      "exchange": null
	    },
	    {
	      "UTCunix": 1605025800,
	      "price": 14800,
	      "amount": 201.75888,
	      "candle": "2020-11-10T16:30:00Z",
	      "exchange": null
	    }
	  ]
	}

**UTCunix:** It's the specific timestamp at which the wall showed up in the orderbook.

**Price:** Rate of the wall.

**Amount:** Amount of the wall.

**Candle:** Timestamp of the candle at which the wall showed up in the orderbook.