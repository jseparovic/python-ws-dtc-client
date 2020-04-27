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
`pip install flask`
`pip install Flask-Sockets`
`pip install gevent-websocket`

For code gen:
`pip install CppHeaderParser`

### Usage
```
usage: example_client.py [-h] -n HOST -p PORT [-r RESTPORT] [-l] [-s]
                         [-u USERNAME] [-x PASSWORD]

DTC Client

optional arguments:
  -h, --help            show this help message and exit
  -n HOST, --host HOST  Websocket Host
  -p PORT, --port PORT  Websocket Port
  -r RESTPORT, --restport RESTPORT
                        REST Server Port
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
If you want to see market data messages in the logs:
```
eg: LOG_DATA=1 LOG_LEVEL=DEBUG ./example_client.py -n localhost -p 11099 -l
```




### REST API
A REST Server will run by default on port 8080 (or specify -r to select a REST port)

Currently the following GET APIs are supported:
```
    ACCOUNT_BALANCE = '/accountbalance'
    CURRENT_POSITIONS = '/currentpositions'
    EXCHANGE_LIST = '/exchangelist'
    HISTORICAL_ACCOUNT_BALANCES = '/historicalaccountbalances'
    HISTORICAL_ORDER_FILLS = '/historicalorderfills'
    SECURITY_DEFINITION = '/securitydefinition'
    TRADE_ACCOUNTS = '/tradeaccounts'
```

Note the full URL would look like (for example):

`http://localhost:8080/api/v1/accountbalance`

If an API requires input, pass in query params (for example):

`http://localhost:8080/api/v1/securitydefinition?Symbol=ESM20_FUT_CME`


### Sample REST Output
```
[
    {
        "Currency": "USD",
        "CurrencyValuePerIncrement": 12.5,
        "Description": "E-MINI S&P 500 FUTURES ES Jun 2020",
        "DisplayPriceMultiplier": 0.009999999776482582,
        "ExchangeSymbol": "ESM20",
        "IsFinalMessage": 1,
        "MinPriceIncrement": 0.25,
        "OpenInterest": 3332460,
        "PriceDisplayFormat": 2,
        "RequestID": 1,
        "SecurityExpirationDate": 1592524800,
        "SecurityType": 1,
        "Symbol": "ESM20_FUT_CME",
        "Type": 507,
        "UnderlyingSymbol": "ES"
    }
]
```



### WS API
Support for Websocket server exists. Currently you can subscribe and unsubscribe to market data.

Connect to the WS Server running on the REST port:
```
ws://localhost:8080/api/v1/marketdata
```

To subscribe to data, Send a JSON message in the following format:
```
{"action": "subscribe", "symbol": "ESM20_FUT_CME"}
```

To unsubscribe to data, Send a JSON message in the following format:
```
{"action": "unsubscribe", "symbol": "ESM20_FUT_CME"}
```

### WS Test
https://www.screencast.com/t/fA4K6paHI2Z


### Sample WS Output
```
[SENT] {"action": "subscribe", "symbol": "ESM20_FUT_CME"}
[RECV] {"action": "subscribe", "symbol": "ESM20_FUT_CME", "success": true}
[RECV] {
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
    "Symbol": "ESM20_FUT_CME",
    "SymbolID": 2114831995,
    "TradingSessionDate": 1587772800,
    "TradingStatus": 4,
    "Type": 104
}
[SENT] {"action": "unsubscribe", "symbol": "ESM20_FUT_CME"}
[RECV] {"action": "unsubscribe", "symbol": "ESM20_FUT_CME", "success": true}
```

Note: There's currently an issue raised with Sierra Charts in regards to the ordering of Market Update fields being incorrect.



### Sample Runtime Output

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
2020-04-25 13:45:56,985 - DTC_Client - DEBUG - Received Heartbeat:
{
    "CurrentDateTime": 1587847557,
    "NumDroppedMessages": 0,
    "Type": 3
}
2020-04-25 13:45:56,985 - DTC_Client - DEBUG - Sending Heartbeat:
{
    "CurrentDateTime": 1587847556.985286,
    "Type": 3
}
2020-04-25 13:46:36,972 - DTC_Client - DEBUG - Received Heartbeat:
{
    "CurrentDateTime": 1587847597,
    "NumDroppedMessages": 0,
    "Type": 3
}
2020-04-25 13:46:36,972 - DTC_Client - DEBUG - Sending Heartbeat:
{
    "CurrentDateTime": 1587847596.972321,
    "Type": 3
}
```


### TODO
Add Trade operations from REST
Websocket Server unit testing during market hours

### Current Code Gen Warning:
```
2020-04-24 22:49:38,368 - CppHeaderParser - WARNING - Ignored struct s_DepthEntry
2020-04-24 22:49:38,369 - CppHeaderParser - WARNING - Ignored struct s_MarketDataUpdateBidAskNoTimeStamp
```
will need to handle these at some stage