
import json
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

