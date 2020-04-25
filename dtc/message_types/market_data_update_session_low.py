
import json
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class MarketDataUpdateSessionLow(BaseMessageType):
    def __init__(self,
                 symbol_id=None,
                 price=None,
                 trading_session_date=None):
        self.Type = MessageTypes.MARKET_DATA_UPDATE_SESSION_LOW
        self.SymbolID = symbol_id
        self.Price = price
        self.TradingSessionDate = trading_session_date

