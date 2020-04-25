
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class DepthEntry(BaseMessageType):
    def __init__(self,
                 price=None,
                 quantity=None):
        self.Type = MessageTypes.DEPTH_ENTRY
        self.Price = price
        self.Quantity = quantity

    @staticmethod
    def from_message(message_obj):
        return DepthEntry(
             price=message_obj.get('Price'),
             quantity=message_obj.get('Quantity')
        )

    @staticmethod
    def get_message_type_name():
        return "DepthEntry"
