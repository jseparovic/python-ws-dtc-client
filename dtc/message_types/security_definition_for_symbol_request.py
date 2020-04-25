
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

    @staticmethod
    def from_message_short(message_obj):
        packet = message_obj.get('F')
        return SecurityDefinitionForSymbolRequest(
             request_id=packet[0],
             symbol=packet[1],
             exchange=packet[2]
        )

    @staticmethod
    def from_message_long(message_obj):
        return SecurityDefinitionForSymbolRequest(
             request_id=message_obj.get('RequestID'),
             symbol=message_obj.get('Symbol'),
             exchange=message_obj.get('Exchange')
        )

    @staticmethod
    def from_message(message_obj):
        if 'F' in message_obj:
            return SecurityDefinitionForSymbolRequest.from_message_short(message_obj)
        else:
            return SecurityDefinitionForSymbolRequest.from_message_long(message_obj)

    @staticmethod
    def get_message_type_name():
        return "SecurityDefinitionForSymbolRequest"
