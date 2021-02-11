Liquidations
==================

Get liquidations data from Binance Futures and Bitmex


.. code-block:: python

    GET /v1/liquidations/?key=<YOUR_KEY>

**PARAMETERS:**

+------------+------------+-----------+
| PARAMETER  | TYPE       | MANDATORY |
+============+============+===========+
| market     | String     |    NO     |
+------------+------------+-----------+
| StartDate  | INT        |    NO     |
+------------+------------+-----------+
| EndDate    | INT        |    NO     |
+------------+------------+-----------+
| amount     | Float      |    NO     |
+------------+------------+-----------+
| Exchange   | String     |    NO     |
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

**StartDate:** Get all the data after a specif timestamp, an integer unix timestamp must be provided.
:code:`/v1/liquidations/?key=<YOUR_KEY>&StartDate=<MARKET>`.

**EndDate:** Get all the data before a specif timestamp, an integer unix timestamp must be provided.
:code:`/v1/liquidations/?key=<YOUR_KEY>&EndDate=<MARKET>`.

**amount:** Get all the liquidations where the amount is bigger than the provided amount. Must be a float 
:code:`/v1/liquidations/?key=<YOUR_KEY>&amount=<MARKET>`.

**Exchange:** Get all the data from a specific exchange. Available exchanges: Binance Futures, Bitmex. :code:`/v1/liquidations/?key=<YOUR_KEY>&exchange=<MARKET>`.

**above_amount:** Get all liquidations above a specified amount. :code:`/v1/liquidations/?key=<YOUR_KEY>&above_amount=<AMOUNT>`.

**below_amount:** Get all liquidations above a specified amount. :code:`/v1/liquidations/?key=<YOUR_KEY>&below_amount=<AMOUNT>`.

**above_price:** Get all liquidations above a specified price. :code:`/v1/liquidations/?key=<YOUR_KEY>&above_price=<PRICE>`.

**below_price:** Get all liquidations below a specified price. :code:`/v1/liquidations/?key=<YOUR_KEY>&below_price=<PRICE>`.