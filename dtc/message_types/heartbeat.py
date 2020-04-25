
import json
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class Heartbeat(BaseMessageType):
    def __init__(self,
                 num_dropped_messages=None,
                 current_date_time=None):
        self.Type = MessageTypes.HEARTBEAT
        self.NumDroppedMessages = num_dropped_messages
        self.CurrentDateTime = current_date_time

