
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class AlertMessage(BaseMessageType):
    def __init__(self,
                 message_text=None,
                 trade_account=None):
        self.Type = MessageTypes.ALERT_MESSAGE
        self.MessageText = message_text
        self.TradeAccount = trade_account

    @staticmethod
    def from_message_short(message_obj):
        packet = message_obj.get('F')
        return AlertMessage(
             message_text=packet[0],
             trade_account=packet[1]
        )

    @staticmethod
    def from_message_long(message_obj):
        return AlertMessage(
             message_text=message_obj.get('MessageText'),
             trade_account=message_obj.get('TradeAccount')
        )

    @staticmethod
    def from_message(message_obj):
        if 'F' in message_obj:
            return AlertMessage.from_message_short(message_obj)
        else:
            return AlertMessage.from_message_long(message_obj)

    @staticmethod
    def get_message_type_name():
        return "AlertMessage"
