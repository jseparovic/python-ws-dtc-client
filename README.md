# A Python Websocket DTC Protocol Client for use with Sierra Chart

Checkout `example_client.py` for an example on how to use the client.

The `DTCClient` class should contain common logic only, and custom logic should go in a child class
(`ExampleDTCClient` for example)

The `dtc` directory contains the generated code based on DTCProtocol.h.

Message Types are here: 
https://github.com/jseparovic/python-ws-dtc-client/tree/master/dtc/message_types

There are generated enums and message types to use in your code


### Dependencies:
`pip install websocket_client`

For code gen:
`pip install CppHeaderParser`

### Usage
```
usage: example_client.py [-h] -n HOST -p PORT [-l] [-s] [-u USERNAME]
                         [-x PASSWORD]

DTC Client

optional arguments:
  -h, --help            show this help message and exit
  -n HOST, --host HOST  Websocket Host
  -p PORT, --port PORT  Websocket Port
  -l, --live            Live trading mode
  -s, --simulated       Simulated trading mode
  -u USERNAME, --username USERNAME
                        Server Username
  -x PASSWORD, --password PASSWORD
                        Server Password

```


### Logging
Set Environment variable `LOG_LEVEL=DEBUG` to see request/responses
```
eg: LOG_LEVEL=DEBUG ./example_client.py -n localhost -p 11099 -l
```

### Sample Output

```
2020-04-25 13:45:16,969 - DTC_Client - INFO - URL: ws://192.168.1.11:21099
2020-04-25 13:45:16,981 - DTC_Client - DEBUG - Sending LogonRequest:
{
    "ClientName": "DTC Client",
    "HeartbeatIntervalInSeconds": 60,
    "Password": "********",
    "ProtocolVersion": 8,
    "TradeMode": 2,
    "Type": 1,
    "Username": "********"
}
2020-04-25 13:45:16,983 - DTC_Client - DEBUG - Received LogonResponse:
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
2020-04-25 13:45:16,984 - DTC_Client - DEBUG - post_login_thread
2020-04-25 13:45:16,984 - DTC_Client - DEBUG - Sending MarketDataRequest:
{
    "RequestAction": 1,
    "Symbol": "ESM20_FUT_CME",
    "SymbolID": 2114831995,
    "Type": 101
}
2020-04-25 13:45:16,984 - DTC_Client - DEBUG - Sending MarketDataRequest:
{
    "RequestAction": 1,
    "Symbol": "CLM20_FUT_NYMEX",
    "SymbolID": 2380550405,
    "Type": 101
}
2020-04-25 13:45:16,985 - DTC_Client - DEBUG - Received MarketDataSnapshot:
{
    "AskPrice": 282825,
    "AskQuantity": 1,
    "BidAskDateTime": 1587762000.001,
    "BidPrice": 282800,
    "BidQuantity": 1,
    "LastTradeDateTime": 1587761999.001,
    "LastTradePrice": 282800,
    "LastTradeVolume": 1,
    "MarketDepthUpdateDateTime": 1587762000.065,
    "OpenInterest": 3332460,
    "SessionHighPrice": 283500,
    "SessionLowPrice": 275525,
    "SessionNumTrades": 4888086,
    "SessionOpenPrice": 277700,
    "SessionSettlementDateTime": 0,
    "SessionSettlementPrice": 282950,
    "SessionVolume": 0,
    "SymbolID": 2114831995,
    "TradingSessionDate": 1587772800,
    "TradingStatus": 2,
    "Type": 104
}
2020-04-25 13:45:16,985 - DTC_Client - DEBUG - on_message_thread
2020-04-25 13:45:16,985 - DTC_Client - DEBUG - Received MarketDataSnapshot:
{
    "AskPrice": 1750,
    "AskQuantity": 6,
    "BidAskDateTime": 1587762000.001,
    "BidPrice": 1702,
    "BidQuantity": 200,
    "LastTradeDateTime": 1587761998.001,
    "LastTradePrice": 1718,
    "LastTradeVolume": 1,
    "MarketDepthUpdateDateTime": 1587762000.081,
    "OpenInterest": 360880,
    "SessionHighPrice": 1797,
    "SessionLowPrice": 1564,
    "SessionNumTrades": 3660069,
    "SessionOpenPrice": 1678,
    "SessionSettlementDateTime": 0,
    "SessionSettlementPrice": 1694,
    "SessionVolume": 0,
    "SymbolID": 2147483647,
    "TradingSessionDate": 1587772800,
    "TradingStatus": 2,
    "Type": 104
}
2020-04-25 13:45:16,985 - DTC_Client - DEBUG - on_message_thread

```


### TODO
Add Flask REST API support and Flask Socket-IO websockets support

### Current Code Gen Warning:
```
2020-04-24 22:49:38,368 - CppHeaderParser - WARNING - Ignored struct s_DepthEntry
2020-04-24 22:49:38,369 - CppHeaderParser - WARNING - Ignored struct s_MarketDataUpdateBidAskNoTimeStamp
```
will need to handle these at some stage