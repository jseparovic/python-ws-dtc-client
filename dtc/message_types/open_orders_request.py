
import json
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

