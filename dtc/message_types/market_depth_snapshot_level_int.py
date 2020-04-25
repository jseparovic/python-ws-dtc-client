
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class MarketDepthSnapshotLevelInt(BaseMessageType):
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
        self.Type = MessageTypes.MARKET_DEPTH_SNAPSHOT_LEVEL_INT
        self.SymbolID = symbol_id
        self.Side = side
        self.Price = price
        self.Quantity = quantity
        self.Level = level
        self.IsFirstMessageInBatch = is_first_message_in_batch
        self.IsLastMessageInBatch = is_last_message_in_batch
        self.DateTime = date_time
        self.NumOrders = num_orders

    @staticmethod
    def from_message_short(message_obj):
        packet = message_obj.get('F')
        return MarketDepthSnapshotLevelInt(
             symbol_id=packet[0],
             side=packet[1],
             price=packet[2],
             quantity=packet[3],
             level=packet[4],
             is_first_message_in_batch=packet[5],
             is_last_message_in_batch=packet[6],
             date_time=packet[7],
             num_orders=packet[8]
        )

    @staticmethod
    def from_message_long(message_obj):
        return MarketDepthSnapshotLevelInt(
             symbol_id=message_obj.get('SymbolID'),
             side=message_obj.get('Side'),
             price=message_obj.get('Price'),
             quantity=message_obj.get('Quantity'),
             level=message_obj.get('Level'),
             is_first_message_in_batch=message_obj.get('IsFirstMessageInBatch'),
             is_last_message_in_batch=message_obj.get('IsLastMessageInBatch'),
             date_time=message_obj.get('DateTime'),
             num_orders=message_obj.get('NumOrders')
        )

    @staticmethod
    def from_message(message_obj):
        if 'F' in message_obj:
            return MarketDepthSnapshotLevelInt.from_message_short(message_obj)
        else:
            return MarketDepthSnapshotLevelInt.from_message_long(message_obj)

    @staticmethod
    def get_message_type_name():
        return "MarketDepthSnapshotLevelInt"
