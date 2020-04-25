
import json
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class MarketDataUpdateSessionVolume(BaseMessageType):
    def __init__(self,
                 symbol_id=None,
                 volume=None,
                 trading_session_date=None,
                 is_final_session_volume=None):
        self.Type = MessageTypes.MARKET_DATA_UPDATE_SESSION_VOLUME
        self.SymbolID = symbol_id
        self.Volume = volume
        self.TradingSessionDate = trading_session_date
        self.IsFinalSessionVolume = is_final_session_volume

