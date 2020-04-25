
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class OpenOrdersRequest(BaseMessageType):
    def __init__(self,
                 request_id=None,
                 request_all_orders=None,
                 server_order_id=None,
                 trade_account=None):
        self.Type = MessageTypes.OPEN_ORDERS_REQUEST
        self.RequestID = request_id
        self.RequestAllOrders = request_all_orders
        self.ServerOrderID = server_order_id
        self.TradeAccount = trade_account

    @staticmethod
    def from_message_short(message_obj):
        packet = message_obj.get('F')
        return OpenOrdersRequest(
             request_id=packet[0],
             request_all_orders=packet[1],
             server_order_id=packet[2],
             trade_account=packet[3]
        )

    @staticmethod
    def from_message_long(message_obj):
        return OpenOrdersRequest(
             request_id=message_obj.get('RequestID'),
             request_all_orders=message_obj.get('RequestAllOrders'),
             server_order_id=message_obj.get('ServerOrderID'),
             trade_account=message_obj.get('TradeAccount')
        )

    @staticmethod
    def from_message(message_obj):
        if 'F' in message_obj:
            return OpenOrdersRequest.from_message_short(message_obj)
        else:
            return OpenOrdersRequest.from_message_long(message_obj)

    @staticmethod
    def get_message_type_name():
        return "OpenOrdersRequest"
