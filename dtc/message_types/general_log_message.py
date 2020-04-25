
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class GeneralLogMessage(BaseMessageType):
    def __init__(self,
                 message_text=None):
        self.Type = MessageTypes.GENERAL_LOG_MESSAGE
        self.MessageText = message_text

    @staticmethod
    def from_message_short(message_obj):
        packet = message_obj.get('F')
        return GeneralLogMessage(
             message_text=packet[0]
        )

    @staticmethod
    def from_message_long(message_obj):
        return GeneralLogMessage(
             message_text=message_obj.get('MessageText')
        )

    @staticmethod
    def from_message(message_obj):
        if 'F' in message_obj:
            return GeneralLogMessage.from_message_short(message_obj)
        else:
            return GeneralLogMessage.from_message_long(message_obj)

    @staticmethod
    def get_message_type_name():
        return "GeneralLogMessage"
