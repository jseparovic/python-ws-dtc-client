
import json
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class MarketDepthSnapshotLevel(BaseMessageType):
    def __init__(self,
                 symbol_id=None,
                 side=None,
                 price=None,
                 quantity=None,
                 level=None,
                 is_first_message_in_batch=None,
                 is_last_message_in_batch=None,
                 date_time=None,
                 num_orders=None):
        self.Type = MessageTypes.MARKET_DEPTH_SNAPSHOT_LEVEL
        self.SymbolID = symbol_id
        self.Side = side
        self.Price = price
        self.Quantity = quantity
        self.Level = level
        self.IsFirstMessageInBatch = is_first_message_in_batch
        self.IsLastMessageInBatch = is_last_message_in_batch
        self.DateTime = date_time
        self.NumOrders = num_orders

