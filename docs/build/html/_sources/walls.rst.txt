Walls
==================

Get orderbook walls data.



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
| StartDate  | INT        |    NO     |
+------------+------------+-----------+
| EndDate    | INT        |    NO     |
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

**exchange (MANDATORY):** Choose an exchange. Available exchanges: Binance, Combined (FTX + Binance + Binance Futures + Bitmex) :code:`/v1/hmc/?key=<YOUR_KEY>&exchange=<EXCHANGE>`.

**timeframe (MANDATORY):** Choose a timeframe. Available timeframes: 5m, 30m. :code:`/v1/hmc/?key=<YOUR_KEY>&timeframe=<TIMEFRAME>`.


**StartDate:** Get all the data after a specif timestamp, an integer unix timestamp must be provided.
:code:`/v1/hmc/?key=<YOUR_KEY>&StartDate=<MARKET>`.

**EndDate:** Get all the data before a specif timestamp, an integer unix timestamp must be provided.
:code:`/v1/hmc/?key=<YOUR_KEY>&EndDate=<MARKET>`.

**above_amount:** Get all liquidations above a specified amount. :code:`/v1/hmc/?key=<YOUR_KEY>&above_amount=<AMOUNT>`.

**below_amount:** Get all liquidations above a specified amount. :code:`/v1/hmc/?key=<YOUR_KEY>&below_amount=<AMOUNT>`.

**above_price:** Get all liquidations above a specified price. :code:`/v1/hmc/?key=<YOUR_KEY>&above_price=<PRICE>`.

**below_price:** Get all liquidations below a specified price. :code:`/v1/hmc/?key=<YOUR_KEY>&below_price=<PRICE>`.