# A Python Websocket DTC Protocol Client for use with Sierra Chart

### Dependencies:
`pip install websocket_client`

For code gen:
`pip install CppHeaderParser`

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

### Logging
Set Environment variable `LOG_LEVEL=DEBUG` to see request/responses
```
eg: LOG_LEVEL=DEBUG ./client.py -n localhost -p 11099
```

### Sample Output

```
2020-04-24 23:04:57,088 - DTC_Client - INFO - URL: ws://192.168.1.11:11099
2020-04-24 23:04:57,101 - DTC_Client - DEBUG - Sending LogonRequest:
{
    "ClientName": "DTC Client",
    "HeartbeatIntervalInSeconds": 60,
    "Password": "********",
    "ProtocolVersion": 8,
    "TradeMode": 3,
    "Type": 1,
    "Username": "********"
}
2020-04-24 23:04:57,104 - DTC_Client - DEBUG - Received LogonResponse:
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
2020-04-24 23:04:57,104 - DTC_Client - DEBUG - Sending AccountBalanceRequest:
{
    "RequestID": 1,
    "Type": 601
}
2020-04-24 23:04:57,105 - DTC_Client - DEBUG - Received AccountBalanceUpdate:
{
    "AccountCurrency": "USD",
    "BalanceAvailableForNewPositions": 2000,
    "CashBalance": 2000,
    "DailyProfitLoss": 0,
    "InfoText": "Current account balance data request",
    "MarginRequirement": 0,
    "MessageNumber": 1,
    "NoAccountBalances": 0,
    "OpenPositionsProfitLoss": 0,
    "RequestID": 1,
    "SecuritiesValue": 0,
    "TotalNumberMessages": 1,
    "TradeAccount": "********",
    "TransactionIdentifier": 2,
    "Type": 600,
    "Unsolicited": 0
}
2020-04-24 23:05:37,138 - DTC_Client - DEBUG - Received Heartbeat:
{
    "Type": 3
}
2020-04-24 23:05:37,138 - DTC_Client - DEBUG - Sending Heartbeat:
{
    "CurrentDateTime": 1587794737.1388001,
    "Type": 3
}

```


### TODO
Heaps. This just shows an example of login and retrieve account balance. It also responds to heartbeats.

Checkout `client.py` for the main code and add logic to send and handle messages in on_message

The `dtc` directory contains the generated code based on DTCProtocol.h.

Message Types are here: 
https://github.com/jseparovic/python-ws-dtc-client/tree/master/dtc/message_types

There are generated enums and message types to use in your code


### Current Code Gen Warning:
```
2020-04-24 22:49:38,368 - CppHeaderParser - WARNING - Ignored struct s_DepthEntry
2020-04-24 22:49:38,369 - CppHeaderParser - WARNING - Ignored struct s_MarketDataUpdateBidAskNoTimeStamp
```
will need to handle these at some stage