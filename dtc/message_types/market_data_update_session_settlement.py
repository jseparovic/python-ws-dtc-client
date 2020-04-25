
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class MarketDataUpdateSessionSettlement(BaseMessageType):
    def __init__(self,
                 symbol_id=None,
                 price=None,
                 date_time=None):
        self.Type = MessageTypes.MARKET_DATA_UPDATE_SESSION_SETTLEMENT
        self.SymbolID = symbol_id
        self.Price = price
        self.DateTime = date_time

    @staticmethod
    def from_message(message_obj):
        return MarketDataUpdateSessionSettlement(
             symbol_id=message_obj.get('SymbolID'),
             price=message_obj.get('Price'),
             date_time=message_obj.get('DateTime')
        )

    @staticmethod
    def get_message_type_name():
        return "MarketDataUpdateSessionSettlement"
