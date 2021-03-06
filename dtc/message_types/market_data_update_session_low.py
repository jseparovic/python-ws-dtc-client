
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

    @staticmethod
    def from_message_short(message_obj):
        packet = message_obj.get('F')
        return MarketDataUpdateSessionLow(
             symbol_id=packet[0],
             price=packet[1],
             trading_session_date=packet[2]
        )

    @staticmethod
    def from_message_long(message_obj):
        return MarketDataUpdateSessionLow(
             symbol_id=message_obj.get('SymbolID'),
             price=message_obj.get('Price'),
             trading_session_date=message_obj.get('TradingSessionDate')
        )

    @staticmethod
    def from_message(message_obj):
        if 'F' in message_obj:
            return MarketDataUpdateSessionLow.from_message_short(message_obj)
        else:
            return MarketDataUpdateSessionLow.from_message_long(message_obj)

    @staticmethod
    def get_message_type_name():
        return "MarketDataUpdateSessionLow"
