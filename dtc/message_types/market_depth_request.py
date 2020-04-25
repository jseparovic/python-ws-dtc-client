
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class MarketDepthRequest(BaseMessageType):
    def __init__(self,
                 request_action=None,
                 symbol_id=None,
                 symbol=None,
                 exchange=None,
                 num_levels=None):
        self.Type = MessageTypes.MARKET_DEPTH_REQUEST
        self.RequestAction = request_action
        self.SymbolID = symbol_id
        self.Symbol = symbol
        self.Exchange = exchange
        self.NumLevels = num_levels

    @staticmethod
    def from_message_short(message_obj):
        packet = message_obj.get('F')
        return MarketDepthRequest(
             request_action=packet[0],
             symbol_id=packet[1],
             symbol=packet[2],
             exchange=packet[3],
             num_levels=packet[4]
        )

    @staticmethod
    def from_message_long(message_obj):
        return MarketDepthRequest(
             request_action=message_obj.get('RequestAction'),
             symbol_id=message_obj.get('SymbolID'),
             symbol=message_obj.get('Symbol'),
             exchange=message_obj.get('Exchange'),
             num_levels=message_obj.get('NumLevels')
        )

    @staticmethod
    def from_message(message_obj):
        if 'F' in message_obj:
            return MarketDepthRequest.from_message_short(message_obj)
        else:
            return MarketDepthRequest.from_message_long(message_obj)

    @staticmethod
    def get_message_type_name():
        return "MarketDepthRequest"
