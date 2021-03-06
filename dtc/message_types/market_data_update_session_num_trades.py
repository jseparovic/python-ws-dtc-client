
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class MarketDataUpdateSessionNumTrades(BaseMessageType):
    def __init__(self,
                 symbol_id=None,
                 num_trades=None,
                 trading_session_date=None):
        self.Type = MessageTypes.MARKET_DATA_UPDATE_SESSION_NUM_TRADES
        self.SymbolID = symbol_id
        self.NumTrades = num_trades
        self.TradingSessionDate = trading_session_date

    @staticmethod
    def from_message_short(message_obj):
        packet = message_obj.get('F')
        return MarketDataUpdateSessionNumTrades(
             symbol_id=packet[0],
             num_trades=packet[1],
             trading_session_date=packet[2]
        )

    @staticmethod
    def from_message_long(message_obj):
        return MarketDataUpdateSessionNumTrades(
             symbol_id=message_obj.get('SymbolID'),
             num_trades=message_obj.get('NumTrades'),
             trading_session_date=message_obj.get('TradingSessionDate')
        )

    @staticmethod
    def from_message(message_obj):
        if 'F' in message_obj:
            return MarketDataUpdateSessionNumTrades.from_message_short(message_obj)
        else:
            return MarketDataUpdateSessionNumTrades.from_message_long(message_obj)

    @staticmethod
    def get_message_type_name():
        return "MarketDataUpdateSessionNumTrades"
