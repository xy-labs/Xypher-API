Market movement
==================

Get how much price moved since a specified timestamp.


.. code-block:: python

    GET /v1/mm/?key=<YOUR_KEY>

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

.. code-block:: python

    GET /v1/mm/?key=<YOUR_KEY>
