

Whalesniper
==================

Get Whalesniper signals.


.. code-block:: python

    GET /v1/whalesniper/?key=<YOUR_KEY>

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
| Amount     | Float      |    NO     |
+------------+------------+-----------+
| Pair       | String     |    NO     |
+------------+------------+-----------+
| Coin       | String     |    NO     |
+------------+------------+-----------+
| Exchange   | String     |    NO     |
+------------+------------+-----------+
| Trend      | String     |    NO     |
+------------+------------+-----------+



**market:** Query WhaleSniper signals for a specific market :code:`/v1/whalesniper/?key=<YOUR_KEY>&market=<MARKET>`.
THE ACCEPTED MARKET FORMAT IS COINPAIR: SO BTCUSDT, ETHUSDT, BNBUSDT and so on

**StartDate:** Get all the signals after a specif timestamp, an integer unix timestamp must be provided.
:code:`/v1/whalesniper/?key=<YOUR_KEY>&StartDate=<MARKET>`.

**EndDate:** Get all the signals before a specif timestamp, an integer unix timestamp must be provided.
:code:`/v1/whalesniper/?key=<YOUR_KEY>&EndDate=<MARKET>`.

**Amount:** Get all the signals where the amount is bigger than the provided amount. Must be a float 
:code:`/v1/whalesniper/?key=<YOUR_KEY>&amount=<MARKET>`.

**Pair:** Get all the signals for a specific pair
:code:`/v1/whalesniper/?key=<YOUR_KEY>&pair=<MARKET>`.

**Coin:** Get all the signals for a specific coin across all the possible pairs
:code:`/v1/whalesniper/?key=<YOUR_KEY>&coin=<MARKET>`.

**Exchange:** Get all the signals from a specific exchange. Available exchanges: Binance, Bitmex, Binance Futures, Bittrex, Huobi. :code:`/v1/whalesniper/?key=<YOUR_KEY>&exchange=<MARKET>`.

**Trend:** Get all the signals with a specific direction: trend or bull.
:code:`/v1/whalesniper/?key=<YOUR_KEY>&trend=<bear/bull>`.