
import json
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class MarketDepthSnapshotLevelFloat(BaseMessageType):
    def __init__(self,
                 symbol_id=None,
                 price=None,
                 quantity=None,
                 num_orders=None,
                 level=None,
                 side=None,
                 final_update_in_batch=None):
        self.Type = MessageTypes.MARKET_DEPTH_SNAPSHOT_LEVEL_FLOAT
        self.SymbolID = symbol_id
        self.Price = price
        self.Quantity = quantity
        self.NumOrders = num_orders
        self.Level = level
        self.Side = side
        self.FinalUpdateInBatch = final_update_in_batch

