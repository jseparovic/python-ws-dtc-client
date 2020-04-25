
import json
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class CancelReplaceOrderInt(BaseMessageType):
    def __init__(self,
                 server_order_id=None,
                 client_order_id=None,
                 price1=None,
                 price2=None,
                 divisor=None,
                 quantity=None,
                 price1_is_set=None,
                 price2_is_set=None,
                 unused=None,
                 time_in_force=None,
                 good_till_date_time=None,
                 update_price1_offset_to_parent=None):
        self.Type = MessageTypes.CANCEL_REPLACE_ORDER_INT
        self.ServerOrderID = server_order_id
        self.ClientOrderID = client_order_id
        self.Price1 = price1
        self.Price2 = price2
        self.Divisor = divisor
        self.Quantity = quantity
        self.Price1IsSet = price1_is_set
        self.Price2IsSet = price2_is_set
        self.Unused = unused
        self.TimeInForce = time_in_force
        self.GoodTillDateTime = good_till_date_time
        self.UpdatePrice1OffsetToParent = update_price1_offset_to_parent

