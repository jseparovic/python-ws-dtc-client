
import json
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class MarketDataUpdateTradeCompact(BaseMessageType):
    def __init__(self,
                 price=None,
                 volume=None,
                 date_time=None,
                 symbol_id=None,
                 at_bid_or_ask=None):
        self.Type = MessageTypes.MARKET_DATA_UPDATE_TRADE_COMPACT
        self.Price = price
        self.Volume = volume
        self.DateTime = date_time
        self.SymbolID = symbol_id
        self.AtBidOrAsk = at_bid_or_ask

