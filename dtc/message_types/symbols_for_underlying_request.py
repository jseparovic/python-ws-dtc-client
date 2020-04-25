
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

    @staticmethod
    def from_message_short(message_obj):
        packet = message_obj.get('F')
        return SymbolsForUnderlyingRequest(
             request_id=packet[0],
             underlying_symbol=packet[1],
             exchange=packet[2],
             security_type=packet[3]
        )

    @staticmethod
    def from_message_long(message_obj):
        return SymbolsForUnderlyingRequest(
             request_id=message_obj.get('RequestID'),
             underlying_symbol=message_obj.get('UnderlyingSymbol'),
             exchange=message_obj.get('Exchange'),
             security_type=message_obj.get('SecurityType')
        )

    @staticmethod
    def from_message(message_obj):
        if 'F' in message_obj:
            return SymbolsForUnderlyingRequest.from_message_short(message_obj)
        else:
            return SymbolsForUnderlyingRequest.from_message_long(message_obj)

    @staticmethod
    def get_message_type_name():
        return "SymbolsForUnderlyingRequest"
