
import json
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class MarketDataFeedStatus(BaseMessageType):
    def __init__(self,
                 status=None):
        self.Type = MessageTypes.MARKET_DATA_FEED_STATUS
        self.Status = status

