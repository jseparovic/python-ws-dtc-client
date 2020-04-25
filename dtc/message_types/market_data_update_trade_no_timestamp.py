
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class MarketDataUpdateTradeNoTimestamp(BaseMessageType):
    def __init__(self,
                 symbol_id=None,
                 price=None,
                 volume=None,
                 at_bid_or_ask=None,
                 unbundled_trade_indicator=None):
        self.Type = MessageTypes.MARKET_DATA_UPDATE_TRADE_NO_TIMESTAMP
        self.SymbolID = symbol_id
        self.Price = price
        self.Volume = volume
        self.AtBidOrAsk = at_bid_or_ask
        self.UnbundledTradeIndicator = unbundled_trade_indicator

    @staticmethod
    def from_message_short(message_obj):
        packet = message_obj.get('F')
        return MarketDataUpdateTradeNoTimestamp(
             symbol_id=packet[0],
             price=packet[1],
             volume=packet[2],
             at_bid_or_ask=packet[3],
             unbundled_trade_indicator=packet[4]
        )

    @staticmethod
    def from_message_long(message_obj):
        return MarketDataUpdateTradeNoTimestamp(
             symbol_id=message_obj.get('SymbolID'),
             price=message_obj.get('Price'),
             volume=message_obj.get('Volume'),
             at_bid_or_ask=message_obj.get('AtBidOrAsk'),
             unbundled_trade_indicator=message_obj.get('UnbundledTradeIndicator')
        )

    @staticmethod
    def from_message(message_obj):
        if 'F' in message_obj:
            return MarketDataUpdateTradeNoTimestamp.from_message_short(message_obj)
        else:
            return MarketDataUpdateTradeNoTimestamp.from_message_long(message_obj)

    @staticmethod
    def get_message_type_name():
        return "MarketDataUpdateTradeNoTimestamp"
