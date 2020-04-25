
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class MarketDataUpdateBidAskCompact(BaseMessageType):
    def __init__(self,
                 bid_price=None,
                 bid_quantity=None,
                 ask_price=None,
                 ask_quantity=None,
                 date_time=None,
                 symbol_id=None):
        self.Type = MessageTypes.MARKET_DATA_UPDATE_BID_ASK_COMPACT
        self.BidPrice = bid_price
        self.BidQuantity = bid_quantity
        self.AskPrice = ask_price
        self.AskQuantity = ask_quantity
        self.DateTime = date_time
        self.SymbolID = symbol_id

    @staticmethod
    def from_message(message_obj):
        return MarketDataUpdateBidAskCompact(
             bid_price=message_obj.get('BidPrice'),
             bid_quantity=message_obj.get('BidQuantity'),
             ask_price=message_obj.get('AskPrice'),
             ask_quantity=message_obj.get('AskQuantity'),
             date_time=message_obj.get('DateTime'),
             symbol_id=message_obj.get('SymbolID')
        )

    @staticmethod
    def get_message_type_name():
        return "MarketDataUpdateBidAskCompact"
