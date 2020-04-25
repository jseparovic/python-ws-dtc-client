
import json
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class MarketDataUpdateLastTradeSnapshot(BaseMessageType):
    def __init__(self,
                 symbol_id=None,
                 last_trade_price=None,
                 last_trade_volume=None,
                 last_trade_date_time=None):
        self.Type = MessageTypes.MARKET_DATA_UPDATE_LAST_TRADE_SNAPSHOT
        self.SymbolID = symbol_id
        self.LastTradePrice = last_trade_price
        self.LastTradeVolume = last_trade_volume
        self.LastTradeDateTime = last_trade_date_time

