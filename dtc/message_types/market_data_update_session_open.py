
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class MarketDataUpdateSessionOpen(BaseMessageType):
    def __init__(self,
                 symbol_id=None,
                 price=None,
                 trading_session_date=None):
        self.Type = MessageTypes.MARKET_DATA_UPDATE_SESSION_OPEN
        self.SymbolID = symbol_id
        self.Price = price
        self.TradingSessionDate = trading_session_date

    @staticmethod
    def from_message(message_obj):
        return MarketDataUpdateSessionOpen(
             symbol_id=message_obj.get('SymbolID'),
             price=message_obj.get('Price'),
             trading_session_date=message_obj.get('TradingSessionDate')
        )

    @staticmethod
    def get_message_type_name():
        return "MarketDataUpdateSessionOpen"
