
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class MarketDataUpdateTradingSessionDate(BaseMessageType):
    def __init__(self,
                 symbol_id=None,
                 date=None):
        self.Type = MessageTypes.MARKET_DATA_UPDATE_TRADING_SESSION_DATE
        self.SymbolID = symbol_id
        self.Date = date

    @staticmethod
    def from_message(message_obj):
        return MarketDataUpdateTradingSessionDate(
             symbol_id=message_obj.get('SymbolID'),
             date=message_obj.get('Date')
        )

    @staticmethod
    def get_message_type_name():
        return "MarketDataUpdateTradingSessionDate"
