
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class MarketDataUpdateOpenInterest(BaseMessageType):
    def __init__(self,
                 symbol_id=None,
                 open_interest=None,
                 trading_session_date=None):
        self.Type = MessageTypes.MARKET_DATA_UPDATE_OPEN_INTEREST
        self.SymbolID = symbol_id
        self.OpenInterest = open_interest
        self.TradingSessionDate = trading_session_date

    @staticmethod
    def from_message(message_obj):
        return MarketDataUpdateOpenInterest(
             symbol_id=message_obj.get('SymbolID'),
             open_interest=message_obj.get('OpenInterest'),
             trading_session_date=message_obj.get('TradingSessionDate')
        )

    @staticmethod
    def get_message_type_name():
        return "MarketDataUpdateOpenInterest"
