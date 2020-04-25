
import json
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class EncodingRequest(BaseMessageType):
    def __init__(self,
                 protocol_version=None,
                 encoding=None,
                 protocol_type=None):
        self.Type = MessageTypes.ENCODING_REQUEST
        self.ProtocolVersion = protocol_version
        self.Encoding = encoding
        self.ProtocolType = protocol_type

