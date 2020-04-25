
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
    def from_message(message_obj):
        return SymbolsForExchangeRequest(
             request_id=message_obj.get('RequestID'),
             exchange=message_obj.get('Exchange'),
             security_type=message_obj.get('SecurityType'),
             request_action=message_obj.get('RequestAction'),
             symbol=message_obj.get('Symbol')
        )

    @staticmethod
    def get_message_type_name():
        return "SymbolsForExchangeRequest"
