
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

    @staticmethod
    def from_message_short(message_obj):
        packet = message_obj.get('F')
        return MarketDepthUpdateLevelFloatWithMilliseconds(
             symbol_id=packet[0],
             date_time=packet[1],
             price=packet[2],
             quantity=packet[3],
             side=packet[4],
             update_type=packet[5],
             num_orders=packet[6],
             final_update_in_batch=packet[7]
        )

    @staticmethod
    def from_message_long(message_obj):
        return MarketDepthUpdateLevelFloatWithMilliseconds(
             symbol_id=message_obj.get('SymbolID'),
             date_time=message_obj.get('DateTime'),
             price=message_obj.get('Price'),
             quantity=message_obj.get('Quantity'),
             side=message_obj.get('Side'),
             update_type=message_obj.get('UpdateType'),
             num_orders=message_obj.get('NumOrders'),
             final_update_in_batch=message_obj.get('FinalUpdateInBatch')
        )

    @staticmethod
    def from_message(message_obj):
        if 'F' in message_obj:
            return MarketDepthUpdateLevelFloatWithMilliseconds.from_message_short(message_obj)
        else:
            return MarketDepthUpdateLevelFloatWithMilliseconds.from_message_long(message_obj)

    @staticmethod
    def get_message_type_name():
        return "MarketDepthUpdateLevelFloatWithMilliseconds"
