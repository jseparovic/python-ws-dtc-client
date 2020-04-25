
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

    @staticmethod
    def from_message(message_obj):
        return CancelReplaceOrderInt(
             server_order_id=message_obj.get('ServerOrderID'),
             client_order_id=message_obj.get('ClientOrderID'),
             price1=message_obj.get('Price1'),
             price2=message_obj.get('Price2'),
             divisor=message_obj.get('Divisor'),
             quantity=message_obj.get('Quantity'),
             price1_is_set=message_obj.get('Price1IsSet'),
             price2_is_set=message_obj.get('Price2IsSet'),
             unused=message_obj.get('Unused'),
             time_in_force=message_obj.get('TimeInForce'),
             good_till_date_time=message_obj.get('GoodTillDateTime'),
             update_price1_offset_to_parent=message_obj.get('UpdatePrice1OffsetToParent')
        )

    @staticmethod
    def get_message_type_name():
        return "CancelReplaceOrderInt"
