
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class MarketDataUpdateTrade(BaseMessageType):
    def __init__(self,
                 symbol_id=None,
                 at_bid_or_ask=None,
                 price=None,
                 volume=None,
                 date_time=None):
        self.Type = MessageTypes.MARKET_DATA_UPDATE_TRADE
        self.SymbolID = symbol_id
        self.AtBidOrAsk = at_bid_or_ask
        self.Price = price
        self.Volume = volume
        self.DateTime = date_time

    @staticmethod
    def from_message(message_obj):
        return MarketDataUpdateTrade(
             symbol_id=message_obj.get('SymbolID'),
             at_bid_or_ask=message_obj.get('AtBidOrAsk'),
             price=message_obj.get('Price'),
             volume=message_obj.get('Volume'),
             date_time=message_obj.get('DateTime')
        )

    @staticmethod
    def get_message_type_name():
        return "MarketDataUpdateTrade"
