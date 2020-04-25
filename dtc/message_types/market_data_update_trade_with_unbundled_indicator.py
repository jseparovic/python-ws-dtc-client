
import json
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class MarketDataUpdateTradeWithUnbundledIndicator(BaseMessageType):
    def __init__(self,
                 symbol_id=None,
                 at_bid_or_ask=None,
                 unbundled_trade_indicator=None,
                 sale_condition=None,
                 reserve_1=None,
                 reserve_2=None,
                 price=None,
                 volume=None,
                 reserve_3=None,
                 date_time=None):
        self.Type = MessageTypes.MARKET_DATA_UPDATE_TRADE_WITH_UNBUNDLED_INDICATOR
        self.SymbolID = symbol_id
        self.AtBidOrAsk = at_bid_or_ask
        self.UnbundledTradeIndicator = unbundled_trade_indicator
        self.SaleCondition = sale_condition
        self.Reserve_1 = reserve_1
        self.Reserve_2 = reserve_2
        self.Price = price
        self.Volume = volume
        self.Reserve_3 = reserve_3
        self.DateTime = date_time

