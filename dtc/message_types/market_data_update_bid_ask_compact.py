
import json
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class MarketDataUpdateBidAskCompact(BaseMessageType):
    def __init__(self,
                 bid_price=None,
                 bid_quantity=None,
                 ask_price=None,
                 ask_quantity=None,
                 date_time=None,
                 symbol_id=None):
        self.Type = MessageTypes.MARKET_DATA_UPDATE_BID_ASK_COMPACT
        self.BidPrice = bid_price
        self.BidQuantity = bid_quantity
        self.AskPrice = ask_price
        self.AskQuantity = ask_quantity
        self.DateTime = date_time
        self.SymbolID = symbol_id

