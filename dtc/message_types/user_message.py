
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class UserMessage(BaseMessageType):
    def __init__(self,
                 user_message=None,
                 is_popup_message=None):
        self.Type = MessageTypes.USER_MESSAGE
        self.UserMessage = user_message
        self.IsPopupMessage = is_popup_message

    @staticmethod
    def from_message_short(message_obj):
        packet = message_obj.get('F')
        return UserMessage(
             user_message=packet[0],
             is_popup_message=packet[1]
        )

    @staticmethod
    def from_message_long(message_obj):
        return UserMessage(
             user_message=message_obj.get('UserMessage'),
             is_popup_message=message_obj.get('IsPopupMessage')
        )

    @staticmethod
    def from_message(message_obj):
        if 'F' in message_obj:
            return UserMessage.from_message_short(message_obj)
        else:
            return UserMessage.from_message_long(message_obj)

    @staticmethod
    def get_message_type_name():
        return "UserMessage"
