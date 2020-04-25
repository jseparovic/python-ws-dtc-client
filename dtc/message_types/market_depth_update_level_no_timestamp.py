
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

    @staticmethod
    def from_message_short(message_obj):
        packet = message_obj.get('F')
        return MarketDepthUpdateLevelNoTimestamp(
             symbol_id=packet[0],
             price=packet[1],
             quantity=packet[2],
             num_orders=packet[3],
             side=packet[4],
             update_type=packet[5],
             final_update_in_batch=packet[6]
        )

    @staticmethod
    def from_message_long(message_obj):
        return MarketDepthUpdateLevelNoTimestamp(
             symbol_id=message_obj.get('SymbolID'),
             price=message_obj.get('Price'),
             quantity=message_obj.get('Quantity'),
             num_orders=message_obj.get('NumOrders'),
             side=message_obj.get('Side'),
             update_type=message_obj.get('UpdateType'),
             final_update_in_batch=message_obj.get('FinalUpdateInBatch')
        )

    @staticmethod
    def from_message(message_obj):
        if 'F' in message_obj:
            return MarketDepthUpdateLevelNoTimestamp.from_message_short(message_obj)
        else:
            return MarketDepthUpdateLevelNoTimestamp.from_message_long(message_obj)

    @staticmethod
    def get_message_type_name():
        return "MarketDepthUpdateLevelNoTimestamp"
