
========
Markets
========

Get Technical Analysis data, used for the /TA command on XypherianBot, and volume data used for the Volume Screener hosted at Xypher.io.


.. code-block:: python

    GET /v1/markets/?key=<YOUR_KEY>

**PARAMETERS:**

+------------+------------+-----------+
| PARAMETER  | TYPE       | MANDATORY |
+============+============+===========+
| market     | String     |    NO     |
+------------+------------+-----------+
| pair       | String     |    NO     |
+------------+------------+-----------+
| coin       | String     |    NO     |
+------------+------------+-----------+
| exchange   | String     |    NO     |
+------------+------------+-----------+
| volume     | Float      |    NO     |
+------------+------------+-----------+



**market:** Get a specific market. :code:`/v1/markets/?key=<YOUR_KEY>&market=<MARKET>`.
THE ACCEPTED MARKET FORMAT IS COINPAIR: SO BTCUSDT, ETHUSDT, BNBUSDT and so on


**pair:** Get all the data for a specific pair
:code:`/v1/markets/?key=<YOUR_KEY>&pair=<MARKET>`.

**coin:** Get all the data for a specific coin across all the possible pairs
:code:`/v1/markets/?key=<YOUR_KEY>&coin=<MARKET>`.

**exchange:** Get a specific exchange. Available exchanges: Binance, Bitmex, Bittrex, Huobi. :code:`/v1/markets/?key=<YOUR_KEY>&exchange=<MARKET>`.

**volume:** Get all markets with an higher volume than provided.
:code:`/v1/markets/?key=<YOUR_KEY>&volume=<VOLUME>`.




Technical Analysis
=====================

Returns techincal analysis data used for the /TA command on XypherianBot.

.. code-block:: python

    GET /v1/markets/ta/?key=<YOUR_KEY>

**PARAMETERS:**

+------------+------------+-----------+
| PARAMETER  | TYPE       | MANDATORY |
+============+============+===========+
| market     | String     |    NO     |
+------------+------------+-----------+
| pair       | String     |    NO     |
+------------+------------+-----------+
| coin       | String     |    NO     |
+------------+------------+-----------+
| exchange   | String     |    NO     |
+------------+------------+-----------+
| volume     | Float      |    NO     |
+------------+------------+-----------+



**market:** Get a specific market. :code:`/v1/markets/?key=<YOUR_KEY>&market=<MARKET>`.
THE ACCEPTED MARKET FORMAT IS COINPAIR: SO BTCUSDT, ETHUSDT, BNBUSDT and so on


**pair:** Get all the data for a specific pair
:code:`/v1/markets/?key=<YOUR_KEY>&pair=<MARKET>`.

**coin:** Get all the data for a specific coin across all the possible pairs
:code:`/v1/markets/?key=<YOUR_KEY>&coin=<MARKET>`.

**exchange:** Get a specific exchange. Available exchanges: Binance, Bitmex, Bittrex, Huobi. :code:`/v1/markets/?key=<YOUR_KEY>&exchange=<MARKET>`.

**volume:** Get all markets with an higher volume than provided.
:code:`/v1/markets/?key=<YOUR_KEY>&volume=<VOLUME>`.



Volume Data
=====================

Returns techincal analysis data used for the /TA command on XypherianBot.

.. code-block:: python

    GET /v1/markets/ta/?key=<YOUR_KEY>


**PARAMETERS:**

+------------+------------+-----------+
| PARAMETER  | TYPE       | MANDATORY |
+============+============+===========+
| market     | String     |    NO     |
+------------+------------+-----------+
| pair       | String     |    NO     |
+------------+------------+-----------+
| coin       | String     |    NO     |
+------------+------------+-----------+
| exchange   | String     |    NO     |
+------------+------------+-----------+
| volume     | Float      |    NO     |
+------------+------------+-----------+



**market:** Get a specific market. :code:`/v1/markets/?key=<YOUR_KEY>&market=<MARKET>`.
THE ACCEPTED MARKET FORMAT IS COINPAIR: SO BTCUSDT, ETHUSDT, BNBUSDT and so on


**pair:** Get all the data for a specific pair
:code:`/v1/markets/?key=<YOUR_KEY>&pair=<MARKET>`.

**coin:** Get all the data for a specific coin across all the possible pairs
:code:`/v1/markets/?key=<YOUR_KEY>&coin=<MARKET>`.

**exchange:** Get a specific exchange. Available exchanges: Binance, Bitmex, Bittrex, Huobi. :code:`/v1/markets/?key=<YOUR_KEY>&exchange=<MARKET>`.

**volume:** Get all markets with an higher volume than provided.
:code:`/v1/markets/?key=<YOUR_KEY>&volume=<VOLUME>`.

**EXAMPLE:** :code:`/v1/markets/?key=<YOUR_KEY>&pair=BTCUSDT`.

