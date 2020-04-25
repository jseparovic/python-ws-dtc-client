
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

    @staticmethod
    def from_message_short(message_obj):
        packet = message_obj.get('F')
        return SymbolsForExchangeRequest(
             request_id=packet[0],
             exchange=packet[1],
             security_type=packet[2],
             request_action=packet[3],
             symbol=packet[4]
        )

    @staticmethod
    def from_message_long(message_obj):
        return SymbolsForExchangeRequest(
             request_id=message_obj.get('RequestID'),
             exchange=message_obj.get('Exchange'),
             security_type=message_obj.get('SecurityType'),
             request_action=message_obj.get('RequestAction'),
             symbol=message_obj.get('Symbol')
        )

    @staticmethod
    def from_message(message_obj):
        if 'F' in message_obj:
            return SymbolsForExchangeRequest.from_message_short(message_obj)
        else:
            return SymbolsForExchangeRequest.from_message_long(message_obj)

    @staticmethod
    def get_message_type_name():
        return "SymbolsForExchangeRequest"
