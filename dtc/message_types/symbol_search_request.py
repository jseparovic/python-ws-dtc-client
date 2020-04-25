
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

    @staticmethod
    def from_message_short(message_obj):
        packet = message_obj.get('F')
        return SymbolSearchRequest(
             request_id=packet[0],
             search_text=packet[1],
             exchange=packet[2],
             security_type=packet[3],
             search_type=packet[4]
        )

    @staticmethod
    def from_message_long(message_obj):
        return SymbolSearchRequest(
             request_id=message_obj.get('RequestID'),
             search_text=message_obj.get('SearchText'),
             exchange=message_obj.get('Exchange'),
             security_type=message_obj.get('SecurityType'),
             search_type=message_obj.get('SearchType')
        )

    @staticmethod
    def from_message(message_obj):
        if 'F' in message_obj:
            return SymbolSearchRequest.from_message_short(message_obj)
        else:
            return SymbolSearchRequest.from_message_long(message_obj)

    @staticmethod
    def get_message_type_name():
        return "SymbolSearchRequest"
