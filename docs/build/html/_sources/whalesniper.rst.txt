

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
| start_date | INT        |    NO     |
+------------+------------+-----------+
| end_date   | INT        |    NO     |
+------------+------------+-----------+
| pair       | String     |    NO     |
+------------+------------+-----------+
| coin       | String     |    NO     |
+------------+------------+-----------+
| exchange   | String     |    NO     |
+------------+------------+-----------+
| trend      | String     |    NO     |
+------------+------------+-----------+



**market:** Query WhaleSniper signals for a specific market :code:`/v1/whalesniper/?key=<YOUR_KEY>&market=<MARKET>`.
THE ACCEPTED MARKET FORMAT IS COINPAIR: SO BTCUSDT, ETHUSDT, BNBUSDT and so on

**start_date:** Get all the signals after a specif timestamp, an integer unix timestamp must be provided.
:code:`/v1/whalesniper/?key=<YOUR_KEY>&start_date=<MARKET>`.

**end_date:** Get all the signals before a specif timestamp, an integer unix timestamp must be provided.
:code:`/v1/whalesniper/?key=<YOUR_KEY>&end_date=<MARKET>`.

**amount:** Get all the signals where the amount is bigger than the provided amount. Must be a float 
:code:`/v1/whalesniper/?key=<YOUR_KEY>&amount=<MARKET>`.

**pair:** Get all the signals for a specific pair
:code:`/v1/whalesniper/?key=<YOUR_KEY>&pair=<MARKET>`.

**Coin:** Get all the signals for a specific coin across all the possible pairs
:code:`/v1/whalesniper/?key=<YOUR_KEY>&coin=<MARKET>`.

**exchange:** Get all the signals from a specific exchange. Available exchanges: Binance, Bitmex, Binance Futures, Bittrex, Huobi. :code:`/v1/whalesniper/?key=<YOUR_KEY>&exchange=<MARKET>`.

**trend:** Get all the signals with a specific direction: trend or bull.
:code:`/v1/whalesniper/?key=<YOUR_KEY>&trend=<bear/bull>`.

**Example:** :code:`/v1/whalesniper/?key=<YOUR-KEY>&market=BTCUSDT&exchange=binance`.

.. code-block:: json

    {"count":127,"next":"http://51.79.25.135/v1/whalesniper/?exchange=binance&key=<YOUR-KEY>&market=BTCUSDT&page=2","previous":null,"results":[{"market":"BTCUSDT","pair":"USDT","coin":"BTC","exchange":"Binance","oldAsk":"39497.92","newAsk":"41971.71","oldBid":"39484.25","newBid":"41955.92","oldVol":"2847768300.27","newVol":"3163939815.24","volDiff":"11","amount":"316171514.97","oldUnix":"1612788200","newUnix":"1612788879","trend":"bull"},{"market":"BTCUSDT","pair":"USDT","coin":"BTC","exchange":"Binance","oldAsk":"33695.39","newAsk":"36831.52","oldBid":"33695.38","newBid":"36821.91","oldVol":"4158620050.73","newVol":"4616238341.94","volDiff":"11","amount":"457618291.21","oldUnix":"1611910065","newUnix":"1611910930","trend":"bull"}]}

