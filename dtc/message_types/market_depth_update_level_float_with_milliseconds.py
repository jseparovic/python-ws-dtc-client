
import json
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class MarketDepthUpdateLevelFloatWithMilliseconds(BaseMessageType):
    def __init__(self,
                 symbol_id=None,
                 date_time=None,
                 price=None,
                 quantity=None,
                 side=None,
                 update_type=None,
                 num_orders=None,
                 final_update_in_batch=None):
        self.Type = MessageTypes.MARKET_DEPTH_UPDATE_LEVEL_FLOAT_WITH_MILLISECONDS
        self.SymbolID = symbol_id
        self.DateTime = date_time
        self.Price = price
        self.Quantity = quantity
        self.Side = side
        self.UpdateType = update_type
        self.NumOrders = num_orders
        self.FinalUpdateInBatch = final_update_in_batch

