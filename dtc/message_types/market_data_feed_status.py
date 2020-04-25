
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class MarketDataFeedStatus(BaseMessageType):
    def __init__(self,
                 status=None):
        self.Type = MessageTypes.MARKET_DATA_FEED_STATUS
        self.Status = status

    @staticmethod
    def from_message_short(message_obj):
        packet = message_obj.get('F')
        return MarketDataFeedStatus(
             status=packet[0]
        )

    @staticmethod
    def from_message_long(message_obj):
        return MarketDataFeedStatus(
             status=message_obj.get('Status')
        )

    @staticmethod
    def from_message(message_obj):
        if 'F' in message_obj:
            return MarketDataFeedStatus.from_message_short(message_obj)
        else:
            return MarketDataFeedStatus.from_message_long(message_obj)

    @staticmethod
    def get_message_type_name():
        return "MarketDataFeedStatus"
