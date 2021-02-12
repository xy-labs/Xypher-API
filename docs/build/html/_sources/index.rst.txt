.. XAPI documentation master file, created by
   sphinx-quickstart on Tue Feb  9 19:52:13 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Xypher API v1 documentation
================================

****************
Getting started
****************

In order to query any API endpoint, you need to get a PRO Xypher account at xypher.io. Once you
did that, get your API token. **Important:** don't share your API token as it is for personal use.

********************
General information
********************
The base endpoint is **https://api.xypher.com/v1/**. The data will always be returned in JSON format.


****************
Limits
****************
The current limit is 70 requests/minute and 7200/hour. Once the limit is violated, a message will be returned. Repeatedly 
violating limits will result in restrictions to the API.



Contents

.. toctree::
   :glob:
   :Caption: Contents

   contact
   auth

  

.. toctree::
   :glob:
   :Caption: Endpoints

   whalesniper
   liquidations
   walls
   markets
   mm
   examples
   
