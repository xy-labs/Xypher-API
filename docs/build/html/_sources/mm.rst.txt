Market movement
==================

Get how much price moved since a specified timestamp.


.. code-block:: python

    GET /v1/mm/?key=<YOUR_KEY>&market<MARKET>&time=<TIME/MINUTES>

**PARAMETERS:**

+------------+------------+-----------+
| PARAMETER  | TYPE       | MANDATORY |
+============+============+===========+
| market     | String     |    YES    |
+------------+------------+-----------+
| exchange   | String     |    NO     |
+------------+------------+-----------+
| time       | INT        |    YES    |
+------------+------------+-----------+

**Important: the time parameter must be provided in minutes.**

**Example:** Check how much did the BITCOIN-USDT market move from 50 minutes ago to now: :code:`/v1/mm/?key=<YOUR_KEY>&market=BTCUSDT&time=50`.

**RESPONSE:**

.. code-block:: json

    {"market":"BTCUSDT","exchange":"binance","current_price":47750.79,"old_price":46810.62,"change_perc":"2.01%"}


