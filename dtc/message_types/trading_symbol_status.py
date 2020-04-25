
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class TradingSymbolStatus(BaseMessageType):
    def __init__(self,
                 symbol_id=None,
                 status=None):
        self.Type = MessageTypes.TRADING_SYMBOL_STATUS
        self.SymbolID = symbol_id
        self.Status = status

    @staticmethod
    def from_message_short(message_obj):
        packet = message_obj.get('F')
        return TradingSymbolStatus(
             symbol_id=packet[0],
             status=packet[1]
        )

    @staticmethod
    def from_message_long(message_obj):
        return TradingSymbolStatus(
             symbol_id=message_obj.get('SymbolID'),
             status=message_obj.get('Status')
        )

    @staticmethod
    def from_message(message_obj):
        if 'F' in message_obj:
            return TradingSymbolStatus.from_message_short(message_obj)
        else:
            return TradingSymbolStatus.from_message_long(message_obj)

    @staticmethod
    def get_message_type_name():
        return "TradingSymbolStatus"
