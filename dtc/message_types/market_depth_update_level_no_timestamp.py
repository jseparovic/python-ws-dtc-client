
import json
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class MarketDepthUpdateLevelNoTimestamp(BaseMessageType):
    def __init__(self,
                 symbol_id=None,
                 price=None,
                 quantity=None,
                 num_orders=None,
                 side=None,
                 update_type=None,
                 final_update_in_batch=None):
        self.Type = MessageTypes.MARKET_DEPTH_UPDATE_LEVEL_NO_TIMESTAMP
        self.SymbolID = symbol_id
        self.Price = price
        self.Quantity = quantity
        self.NumOrders = num_orders
        self.Side = side
        self.UpdateType = update_type
        self.FinalUpdateInBatch = final_update_in_batch

