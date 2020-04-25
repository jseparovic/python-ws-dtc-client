
import json
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class MarketDataUpdateBidAskNoTimeStamp(BaseMessageType):
    def __init__(self,
                 symbol_id=None,
                 bid_price=None,
                 bid_quantity=None,
                 ask_price=None,
                 ask_quantity=None):
        self.Type = MessageTypes.MARKET_DATA_UPDATE_BID_ASK_NO_TIME_STAMP
        self.SymbolID = symbol_id
        self.BidPrice = bid_price
        self.BidQuantity = bid_quantity
        self.AskPrice = ask_price
        self.AskQuantity = ask_quantity

