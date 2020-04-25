
import json
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class TradingSymbolStatus(BaseMessageType):
    def __init__(self,
                 symbol_id=None,
                 status=None):
        self.Type = MessageTypes.TRADING_SYMBOL_STATUS
        self.SymbolID = symbol_id
        self.Status = status

