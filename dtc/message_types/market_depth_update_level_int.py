
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class MarketDepthUpdateLevelInt(BaseMessageType):
    def __init__(self,
                 symbol_id=None,
                 side=None,
                 price=None,
                 quantity=None,
                 update_type=None,
                 date_time=None,
                 num_orders=None):
        self.Type = MessageTypes.MARKET_DEPTH_UPDATE_LEVEL_INT
        self.SymbolID = symbol_id
        self.Side = side
        self.Price = price
        self.Quantity = quantity
        self.UpdateType = update_type
        self.DateTime = date_time
        self.NumOrders = num_orders

    @staticmethod
    def from_message_short(message_obj):
        packet = message_obj.get('F')
        return MarketDepthUpdateLevelInt(
             symbol_id=packet[0],
             side=packet[1],
             price=packet[2],
             quantity=packet[3],
             update_type=packet[4],
             date_time=packet[5],
             num_orders=packet[6]
        )

    @staticmethod
    def from_message_long(message_obj):
        return MarketDepthUpdateLevelInt(
             symbol_id=message_obj.get('SymbolID'),
             side=message_obj.get('Side'),
             price=message_obj.get('Price'),
             quantity=message_obj.get('Quantity'),
             update_type=message_obj.get('UpdateType'),
             date_time=message_obj.get('DateTime'),
             num_orders=message_obj.get('NumOrders')
        )

    @staticmethod
    def from_message(message_obj):
        if 'F' in message_obj:
            return MarketDepthUpdateLevelInt.from_message_short(message_obj)
        else:
            return MarketDepthUpdateLevelInt.from_message_long(message_obj)

    @staticmethod
    def get_message_type_name():
        return "MarketDepthUpdateLevelInt"
