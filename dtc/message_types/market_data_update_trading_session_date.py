
import json
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class MarketDataUpdateTradingSessionDate(BaseMessageType):
    def __init__(self,
                 symbol_id=None,
                 date=None):
        self.Type = MessageTypes.MARKET_DATA_UPDATE_TRADING_SESSION_DATE
        self.SymbolID = symbol_id
        self.Date = date

