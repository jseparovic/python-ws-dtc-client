
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class EncodingResponse(BaseMessageType):
    def __init__(self,
                 protocol_version=None,
                 encoding=None,
                 protocol_type=None):
        self.Type = MessageTypes.ENCODING_RESPONSE
        self.ProtocolVersion = protocol_version
        self.Encoding = encoding
        self.ProtocolType = protocol_type

    @staticmethod
    def from_message_short(message_obj):
        packet = message_obj.get('F')
        return EncodingResponse(
             protocol_version=packet[0],
             encoding=packet[1],
             protocol_type=packet[2]
        )

    @staticmethod
    def from_message_long(message_obj):
        return EncodingResponse(
             protocol_version=message_obj.get('ProtocolVersion'),
             encoding=message_obj.get('Encoding'),
             protocol_type=message_obj.get('ProtocolType')
        )

    @staticmethod
    def from_message(message_obj):
        if 'F' in message_obj:
            return EncodingResponse.from_message_short(message_obj)
        else:
            return EncodingResponse.from_message_long(message_obj)

    @staticmethod
    def get_message_type_name():
        return "EncodingResponse"
