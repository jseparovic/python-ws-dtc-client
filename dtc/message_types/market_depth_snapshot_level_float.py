
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

    @staticmethod
    def from_message(message_obj):
        return MarketDepthSnapshotLevelFloat(
             symbol_id=message_obj.get('SymbolID'),
             price=message_obj.get('Price'),
             quantity=message_obj.get('Quantity'),
             num_orders=message_obj.get('NumOrders'),
             level=message_obj.get('Level'),
             side=message_obj.get('Side'),
             final_update_in_batch=message_obj.get('FinalUpdateInBatch')
        )

    @staticmethod
    def get_message_type_name():
        return "MarketDepthSnapshotLevelFloat"
