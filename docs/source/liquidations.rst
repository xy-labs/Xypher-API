Liquidations
==================

Get liquidations data from Binance Futures and Bitmex.


.. code-block:: python

    GET /v1/liquidations/?key=<YOUR_KEY>

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
| amount     | Float      |    NO     |
+------------+------------+-----------+
| exchange   | String     |    NO     |
+------------+------------+-----------+
| side       | String     |    NO     |
+------------+------------+-----------+
|above_amount| Float      |    NO     |
+------------+------------+-----------+
|below_amount| Float      |    NO     |
+------------+------------+-----------+
|above_price | Float      |    NO     |
+------------+------------+-----------+
|below_price | Float      |    NO     |
+------------+------------+-----------+



**market:** Query liquidations data for a specific market :code:`/v1/liquidations/?key=<YOUR_KEY>&market=<MARKET>`.
THE ACCEPTED MARKET FORMAT IS COINPAIR: SO XBTUSDT, ETHUSDT and so on

**start_date:** Get all the data after a specif timestamp, an integer unix timestamp must be provided.
:code:`/v1/liquidations/?key=<YOUR_KEY>&start_date=<MARKET>`.

**end_date:** Get all the data before a specif timestamp, an integer unix timestamp must be provided.
:code:`/v1/liquidations/?key=<YOUR_KEY>&end_date=<MARKET>`.

**amount:** Get all the liquidations where the amount is bigger than the provided amount. Must be a float 
:code:`/v1/liquidations/?key=<YOUR_KEY>&amount=<MARKET>`.

**exchange:** Get all the data from a specific exchange. :code:`/v1/liquidations/?key=<YOUR_KEY>&exchange=<EXCHANGE>`. Exchange can be  :code:`bitmex` or :code:`binance_futures`

**side:** Choose a side. :code:`/v1/liquidations/?key=<YOUR_KEY>&side=<SIDE>`. Side can be  :code:`Short` or :code:`Long`

**above_amount:** Get all liquidations above a specified amount. :code:`/v1/liquidations/?key=<YOUR_KEY>&above_amount=<AMOUNT>`.

**below_amount:** Get all liquidations above a specified amount. :code:`/v1/liquidations/?key=<YOUR_KEY>&below_amount=<AMOUNT>`.

**above_price:** Get all liquidations above a specified price. :code:`/v1/liquidations/?key=<YOUR_KEY>&above_price=<PRICE>`.

**below_price:** Get all liquidations below a specified price. :code:`/v1/liquidations/?key=<YOUR_KEY>&below_price=<PRICE>`.


**EXAMPLE:**  
:code:`/v1/liquidations/?key=<YOUR_KEY>&market=BTCUSDT`.

.. code-block:: json

	{
	  "count": 1371311,
	  "next": "http://api.xypher.io/v1/liquidations/?key=<YOUR-KEY>&market=BTCUSDT&page=2",
	  "previous": null,
	  "results": [
	    {
	      "market": "BTCUSDT",
	      "exchange": "Binance",
	      "side": "Long",
	      "amount": "1100",
	      "price": "47839.49",
	      "unixtime": 1613087216
	    },
	    {
	      "market": "BTCUSDT",
	      "exchange": "Binance",
	      "side": "Short",
	      "amount": "480",
	      "price": "48057.39",
	      "unixtime": 1613086429
	    },
	    {
	      "market": "BTCUSDT",
	      "exchange": "Binance",
	      "side": "Short",
	      "amount": "4661",
	      "price": "48054.11",
	      "unixtime": 1613086429
	    },
	    {
	      "market": "BTCUSDT",
	      "exchange": "Binance",
	      "side": "Short",
	      "amount": "14709",
	      "price": "48069.89",
	      "unixtime": 1613086427
	    }
	  ]
	}