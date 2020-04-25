
import json
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class Logoff(BaseMessageType):
    def __init__(self,
                 reason=None,
                 do_not_reconnect=None):
        self.Type = MessageTypes.LOGOFF
        self.Reason = reason
        self.DoNotReconnect = do_not_reconnect

