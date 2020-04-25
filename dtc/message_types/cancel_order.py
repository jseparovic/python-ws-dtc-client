
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class CancelOrder(BaseMessageType):
    def __init__(self,
                 server_order_id=None,
                 client_order_id=None):
        self.Type = MessageTypes.CANCEL_ORDER
        self.ServerOrderID = server_order_id
        self.ClientOrderID = client_order_id

    @staticmethod
    def from_message_short(message_obj):
        packet = message_obj.get('F')
        return CancelOrder(
             server_order_id=packet[0],
             client_order_id=packet[1]
        )

    @staticmethod
    def from_message_long(message_obj):
        return CancelOrder(
             server_order_id=message_obj.get('ServerOrderID'),
             client_order_id=message_obj.get('ClientOrderID')
        )

    @staticmethod
    def from_message(message_obj):
        if 'F' in message_obj:
            return CancelOrder.from_message_short(message_obj)
        else:
            return CancelOrder.from_message_long(message_obj)

    @staticmethod
    def get_message_type_name():
        return "CancelOrder"
