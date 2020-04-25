
import json
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class SymbolsForUnderlyingRequest(BaseMessageType):
    def __init__(self,
                 request_id=None,
                 underlying_symbol=None,
                 exchange=None,
                 security_type=None):
        self.Type = MessageTypes.SYMBOLS_FOR_UNDERLYING_REQUEST
        self.RequestID = request_id
        self.UnderlyingSymbol = underlying_symbol
        self.Exchange = exchange
        self.SecurityType = security_type

