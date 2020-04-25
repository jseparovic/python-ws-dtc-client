
import json
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class SecurityDefinitionReject(BaseMessageType):
    def __init__(self,
                 request_id=None,
                 reject_text=None):
        self.Type = MessageTypes.SECURITY_DEFINITION_REJECT
        self.RequestID = request_id
        self.RejectText = reject_text

