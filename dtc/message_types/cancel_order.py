
import json
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class CancelOrder(BaseMessageType):
    def __init__(self,
                 server_order_id=None,
                 client_order_id=None):
        self.Type = MessageTypes.CANCEL_ORDER
        self.ServerOrderID = server_order_id
        self.ClientOrderID = client_order_id

