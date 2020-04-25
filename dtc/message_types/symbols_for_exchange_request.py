
import json
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class SymbolsForExchangeRequest(BaseMessageType):
    def __init__(self,
                 request_id=None,
                 exchange=None,
                 security_type=None,
                 request_action=None,
                 symbol=None):
        self.Type = MessageTypes.SYMBOLS_FOR_EXCHANGE_REQUEST
        self.RequestID = request_id
        self.Exchange = exchange
        self.SecurityType = security_type
        self.RequestAction = request_action
        self.Symbol = symbol

