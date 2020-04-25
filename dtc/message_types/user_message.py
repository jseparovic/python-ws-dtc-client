
import json
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class UserMessage(BaseMessageType):
    def __init__(self,
                 user_message=None,
                 is_popup_message=None):
        self.Type = MessageTypes.USER_MESSAGE
        self.UserMessage = user_message
        self.IsPopupMessage = is_popup_message

