
import json
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class MarketDataUpdateTradeNoTimestamp(BaseMessageType):
    def __init__(self,
                 symbol_id=None,
                 price=None,
                 volume=None,
                 at_bid_or_ask=None,
                 unbundled_trade_indicator=None):
        self.Type = MessageTypes.MARKET_DATA_UPDATE_TRADE_NO_TIMESTAMP
        self.SymbolID = symbol_id
        self.Price = price
        self.Volume = volume
        self.AtBidOrAsk = at_bid_or_ask
        self.UnbundledTradeIndicator = unbundled_trade_indicator

