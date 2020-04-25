
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

    @staticmethod
    def from_message(message_obj):
        return LogonResponse(
             protocol_version=message_obj.get('ProtocolVersion'),
             result=message_obj.get('Result'),
             result_text=message_obj.get('ResultText'),
             reconnect_address=message_obj.get('ReconnectAddress'),
             integer_1=message_obj.get('Integer_1'),
             server_name=message_obj.get('ServerName'),
             market_depth_updates_best_bid_and_ask=message_obj.get('MarketDepthUpdatesBestBidAndAsk'),
             trading_is_supported=message_obj.get('TradingIsSupported'),
             o_c_o_orders_supported=message_obj.get('OCOOrdersSupported'),
             order_cancel_replace_supported=message_obj.get('OrderCancelReplaceSupported'),
             symbol_exchange_delimiter=message_obj.get('SymbolExchangeDelimiter'),
             security_definitions_supported=message_obj.get('SecurityDefinitionsSupported'),
             historical_price_data_supported=message_obj.get('HistoricalPriceDataSupported'),
             resubscribe_when_market_data_feed_available=message_obj.get('ResubscribeWhenMarketDataFeedAvailable'),
             market_depth_is_supported=message_obj.get('MarketDepthIsSupported'),
             one_historical_price_data_request_per_connection=message_obj.get('OneHistoricalPriceDataRequestPerConnection'),
             bracket_orders_supported=message_obj.get('BracketOrdersSupported'),
             use_integer_price_order_messages=message_obj.get('UseIntegerPriceOrderMessages'),
             uses_multiple_positions_per_symbol_and_trade_account=message_obj.get('UsesMultiplePositionsPerSymbolAndTradeAccount'),
             market_data_supported=message_obj.get('MarketDataSupported')
        )

    @staticmethod
    def get_message_type_name():
        return "LogonResponse"
