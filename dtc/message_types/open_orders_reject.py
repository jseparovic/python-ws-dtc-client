
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class OpenOrdersReject(BaseMessageType):
    def __init__(self,
                 request_id=None,
                 reject_text=None):
        self.Type = MessageTypes.OPEN_ORDERS_REJECT
        self.RequestID = request_id
        self.RejectText = reject_text

    @staticmethod
    def from_message(message_obj):
        return OpenOrdersReject(
             request_id=message_obj.get('RequestID'),
             reject_text=message_obj.get('RejectText')
        )

    @staticmethod
    def get_message_type_name():
        return "OpenOrdersReject"
