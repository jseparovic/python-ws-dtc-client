
import json
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class SymbolSearchRequest(BaseMessageType):
    def __init__(self,
                 request_id=None,
                 search_text=None,
                 exchange=None,
                 security_type=None,
                 search_type=None):
        self.Type = MessageTypes.SYMBOL_SEARCH_REQUEST
        self.RequestID = request_id
        self.SearchText = search_text
        self.Exchange = exchange
        self.SecurityType = security_type
        self.SearchType = search_type

