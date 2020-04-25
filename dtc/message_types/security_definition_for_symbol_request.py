
import json
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class SecurityDefinitionForSymbolRequest(BaseMessageType):
    def __init__(self,
                 request_id=None,
                 symbol=None,
                 exchange=None):
        self.Type = MessageTypes.SECURITY_DEFINITION_FOR_SYMBOL_REQUEST
        self.RequestID = request_id
        self.Symbol = symbol
        self.Exchange = exchange

