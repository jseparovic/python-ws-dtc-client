
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

    @staticmethod
    def from_message_short(message_obj):
        packet = message_obj.get('F')
        return MarketDataUpdateLastTradeSnapshot(
             symbol_id=packet[0],
             last_trade_price=packet[1],
             last_trade_volume=packet[2],
             last_trade_date_time=packet[3]
        )

    @staticmethod
    def from_message_long(message_obj):
        return MarketDataUpdateLastTradeSnapshot(
             symbol_id=message_obj.get('SymbolID'),
             last_trade_price=message_obj.get('LastTradePrice'),
             last_trade_volume=message_obj.get('LastTradeVolume'),
             last_trade_date_time=message_obj.get('LastTradeDateTime')
        )

    @staticmethod
    def from_message(message_obj):
        if 'F' in message_obj:
            return MarketDataUpdateLastTradeSnapshot.from_message_short(message_obj)
        else:
            return MarketDataUpdateLastTradeSnapshot.from_message_long(message_obj)

    @staticmethod
    def get_message_type_name():
        return "MarketDataUpdateLastTradeSnapshot"
