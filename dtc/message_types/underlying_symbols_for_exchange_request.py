
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class UnderlyingSymbolsForExchangeRequest(BaseMessageType):
    def __init__(self,
                 request_id=None,
                 exchange=None,
                 security_type=None):
        self.Type = MessageTypes.UNDERLYING_SYMBOLS_FOR_EXCHANGE_REQUEST
        self.RequestID = request_id
        self.Exchange = exchange
        self.SecurityType = security_type

    @staticmethod
    def from_message_short(message_obj):
        packet = message_obj.get('F')
        return UnderlyingSymbolsForExchangeRequest(
             request_id=packet[0],
             exchange=packet[1],
             security_type=packet[2]
        )

    @staticmethod
    def from_message_long(message_obj):
        return UnderlyingSymbolsForExchangeRequest(
             request_id=message_obj.get('RequestID'),
             exchange=message_obj.get('Exchange'),
             security_type=message_obj.get('SecurityType')
        )

    @staticmethod
    def from_message(message_obj):
        if 'F' in message_obj:
            return UnderlyingSymbolsForExchangeRequest.from_message_short(message_obj)
        else:
            return UnderlyingSymbolsForExchangeRequest.from_message_long(message_obj)

    @staticmethod
    def get_message_type_name():
        return "UnderlyingSymbolsForExchangeRequest"
