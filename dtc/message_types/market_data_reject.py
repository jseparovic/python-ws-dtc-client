
import json
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class MarketDataReject(BaseMessageType):
    def __init__(self,
                 symbol_id=None,
                 reject_text=None):
        self.Type = MessageTypes.MARKET_DATA_REJECT
        self.SymbolID = symbol_id
        self.RejectText = reject_text

