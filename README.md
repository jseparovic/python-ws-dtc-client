# python-ws-dtc-client

### Dependencies:

pip install websocket_client


### Usage
```
usage: client.py [-h] -n HOST -p PORT [-u USERNAME] [-x PASSWORD]

DTC Client

optional arguments:
  -h, --help            show this help message and exit
  -n HOST, --host HOST  Websocket Host
  -p PORT, --port PORT  Websocket Port
  -u USERNAME, --username USERNAME
                        Server Username
  -x PASSWORD, --password PASSWORD
                        Server Password
```


### TODO
Heaps. This just shows an example of login so far.

Checkout client.py for the main code and add logic to send and handle messages in on_message

The 'dtc' directory contains the generated code based on DTCProtocol.h. 

There are generated enums and message types to use in your code


### Sample Output

```
2020-04-24 22:35:34,358 - DTC_Client - INFO - URL: ws://192.168.1.11:11099
2020-04-24 22:35:34,371 - DTC_Client - INFO - Sending LogonRequest:
{
    "ClientName": "DTC Client",
    "HeartbeatIntervalInSeconds": 60,
    "Password": "",
    "ProtocolVersion": 8,
    "TradeMode": 3,
    "Type": 1,
    "Username": ""
}
2020-04-24 22:35:34,373 - DTC_Client - INFO - Received LogonResponse:
{
    "BracketOrdersSupported": 0,
    "HistoricalPriceDataSupported": 0,
    "Integer_1": 0,
    "MarketDataSupported": 1,
    "MarketDepthIsSupported": 1,
    "MarketDepthUpdatesBestBidAndAsk": 0,
    "OCOOrdersSupported": 0,
    "OneHistoricalPriceDataRequestPerConnection": 0,
    "OrderCancelReplaceSupported": 0,
    "ProtocolVersion": 8,
    "ReconnectAddress": "",
    "ResubscribeWhenMarketDataFeedAvailable": 0,
    "Result": 1,
    "ResultText": "Connected to SC DTC Protocol server. Service=sc_futures.dtc.trading|SymbolSettings=sc_futures.dtc.trading",
    "SecurityDefinitionsSupported": 1,
    "ServerName": "SC DTC Server",
    "SymbolExchangeDelimiter": "",
    "TradingIsSupported": 0,
    "Type": 2,
    "UseIntegerPriceOrderMessages": 0,
    "UsesMultiplePositionsPerSymbolAndTradeAccount": 0
}
2020-04-24 22:36:14,375 - DTC_Client - INFO - Received Heartbeat:
{
    "Type": 3
}
2020-04-24 22:36:14,375 - DTC_Client - INFO - Sending Heartbeat:
{
    "CurrentDateTime": 1587792974.375215,
    "Type": 3
}
2020-04-24 22:36:54,362 - DTC_Client - INFO - Received Heartbeat:
{
    "Type": 3
}
2020-04-24 22:36:54,363 - DTC_Client - INFO - Sending Heartbeat:
{
    "CurrentDateTime": 1587793014.362962,
    "Type": 3
}

```