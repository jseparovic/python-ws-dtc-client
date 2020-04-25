
import json
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class GeneralLogMessage(BaseMessageType):
    def __init__(self,
                 message_text=None):
        self.Type = MessageTypes.GENERAL_LOG_MESSAGE
        self.MessageText = message_text

