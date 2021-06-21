============================
Authentication & Pagination
============================

In order to view any endpoint, you'll need to include your API token in your GET request.

.. code-block:: python

    https://api.xypher.io/v1/<endpoint>?key=<YOUR_KEY>

**Make sure to send any request over HTTPS, else your request will be ignored.**



Pagination
============================

The API uses pagination. By default, each page is 50 records long.

In order to navigate across the pages, add a :code:`page` parameter to your GET request. **Example:** 
:code:`/v1/whalesniper/?key=<YOUR-KEY>&market=BTCUSDT&page=2`

The API is still in experimental phase, so these settings may change in the future.