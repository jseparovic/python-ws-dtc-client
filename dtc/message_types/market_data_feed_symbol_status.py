
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class MarketDataFeedSymbolStatus(BaseMessageType):
    def __init__(self,
                 symbol_id=None,
                 status=None):
        self.Type = MessageTypes.MARKET_DATA_FEED_SYMBOL_STATUS
        self.SymbolID = symbol_id
        self.Status = status

    @staticmethod
    def from_message_short(message_obj):
        packet = message_obj.get('F')
        return MarketDataFeedSymbolStatus(
             symbol_id=packet[0],
             status=packet[1]
        )

    @staticmethod
    def from_message_long(message_obj):
        return MarketDataFeedSymbolStatus(
             symbol_id=message_obj.get('SymbolID'),
             status=message_obj.get('Status')
        )

    @staticmethod
    def from_message(message_obj):
        if 'F' in message_obj:
            return MarketDataFeedSymbolStatus.from_message_short(message_obj)
        else:
            return MarketDataFeedSymbolStatus.from_message_long(message_obj)

    @staticmethod
    def get_message_type_name():
        return "MarketDataFeedSymbolStatus"
