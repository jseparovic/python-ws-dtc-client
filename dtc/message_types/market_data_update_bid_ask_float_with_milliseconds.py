
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class MarketDataUpdateBidAskFloatWithMilliseconds(BaseMessageType):
    def __init__(self,
                 symbol_id=None,
                 bid_price=None,
                 bid_quantity=None,
                 ask_price=None,
                 ask_quantity=None,
                 date_time=None):
        self.Type = MessageTypes.MARKET_DATA_UPDATE_BID_ASK_FLOAT_WITH_MILLISECONDS
        self.SymbolID = symbol_id
        self.BidPrice = bid_price
        self.BidQuantity = bid_quantity
        self.AskPrice = ask_price
        self.AskQuantity = ask_quantity
        self.DateTime = date_time

    @staticmethod
    def from_message(message_obj):
        return MarketDataUpdateBidAskFloatWithMilliseconds(
             symbol_id=message_obj.get('SymbolID'),
             bid_price=message_obj.get('BidPrice'),
             bid_quantity=message_obj.get('BidQuantity'),
             ask_price=message_obj.get('AskPrice'),
             ask_quantity=message_obj.get('AskQuantity'),
             date_time=message_obj.get('DateTime')
        )

    @staticmethod
    def get_message_type_name():
        return "MarketDataUpdateBidAskFloatWithMilliseconds"
