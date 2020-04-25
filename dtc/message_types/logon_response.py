
import json
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class LogonResponse(BaseMessageType):
    def __init__(self,
                 protocol_version=None,
                 result=None,
                 result_text=None,
                 reconnect_address=None,
                 integer_1=None,
                 server_name=None,
                 market_depth_updates_best_bid_and_ask=None,
                 trading_is_supported=None,
                 o_c_o_orders_supported=None,
                 order_cancel_replace_supported=None,
                 symbol_exchange_delimiter=None,
                 security_definitions_supported=None,
                 historical_price_data_supported=None,
                 resubscribe_when_market_data_feed_available=None,
                 market_depth_is_supported=None,
                 one_historical_price_data_request_per_connection=None,
                 bracket_orders_supported=None,
                 use_integer_price_order_messages=None,
                 uses_multiple_positions_per_symbol_and_trade_account=None,
                 market_data_supported=None):
        self.Type = MessageTypes.LOGON_RESPONSE
        self.ProtocolVersion = protocol_version
        self.Result = result
        self.ResultText = result_text
        self.ReconnectAddress = reconnect_address
        self.Integer_1 = integer_1
        self.ServerName = server_name
        self.MarketDepthUpdatesBestBidAndAsk = market_depth_updates_best_bid_and_ask
        self.TradingIsSupported = trading_is_supported
        self.OCOOrdersSupported = o_c_o_orders_supported
        self.OrderCancelReplaceSupported = order_cancel_replace_supported
        self.SymbolExchangeDelimiter = symbol_exchange_delimiter
        self.SecurityDefinitionsSupported = security_definitions_supported
        self.HistoricalPriceDataSupported = historical_price_data_supported
        self.ResubscribeWhenMarketDataFeedAvailable = resubscribe_when_market_data_feed_available
        self.MarketDepthIsSupported = market_depth_is_supported
        self.OneHistoricalPriceDataRequestPerConnection = one_historical_price_data_request_per_connection
        self.BracketOrdersSupported = bracket_orders_supported
        self.UseIntegerPriceOrderMessages = use_integer_price_order_messages
        self.UsesMultiplePositionsPerSymbolAndTradeAccount = uses_multiple_positions_per_symbol_and_trade_account
        self.MarketDataSupported = market_data_supported

