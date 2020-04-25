
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class ExchangeListResponse(BaseMessageType):
    def __init__(self,
                 request_id=None,
                 exchange=None,
                 is_final_message=None,
                 description=None):
        self.Type = MessageTypes.EXCHANGE_LIST_RESPONSE
        self.RequestID = request_id
        self.Exchange = exchange
        self.IsFinalMessage = is_final_message
        self.Description = description

    @staticmethod
    def from_message_short(message_obj):
        packet = message_obj.get('F')
        return ExchangeListResponse(
             request_id=packet[0],
             exchange=packet[1],
             is_final_message=packet[2],
             description=packet[3]
        )

    @staticmethod
    def from_message_long(message_obj):
        return ExchangeListResponse(
             request_id=message_obj.get('RequestID'),
             exchange=message_obj.get('Exchange'),
             is_final_message=message_obj.get('IsFinalMessage'),
             description=message_obj.get('Description')
        )

    @staticmethod
    def from_message(message_obj):
        if 'F' in message_obj:
            return ExchangeListResponse.from_message_short(message_obj)
        else:
            return ExchangeListResponse.from_message_long(message_obj)

    @staticmethod
    def get_message_type_name():
        return "ExchangeListResponse"
