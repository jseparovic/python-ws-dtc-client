
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
    def from_message(message_obj):
        return MarketDataUpdateSessionNumTrades(
             symbol_id=message_obj.get('SymbolID'),
             num_trades=message_obj.get('NumTrades'),
             trading_session_date=message_obj.get('TradingSessionDate')
        )

    @staticmethod
    def get_message_type_name():
        return "MarketDataUpdateSessionNumTrades"
