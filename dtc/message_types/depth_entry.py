
import json
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class DepthEntry(BaseMessageType):
    def __init__(self,
                 price=None,
                 quantity=None):
        self.Type = MessageTypes.DEPTH_ENTRY
        self.Price = price
        self.Quantity = quantity

