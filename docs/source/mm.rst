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


**Example:** :code:`/v1/mm/?key=<YOUR_KEY>&market=BTCUSDT&time=1613046249`.

.. code-block:: python

    GET /v1/mm/?key=<YOUR_KEY>
