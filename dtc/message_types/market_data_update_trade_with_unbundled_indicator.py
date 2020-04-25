
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class MarketDataUpdateTradeWithUnbundledIndicator(BaseMessageType):
    def __init__(self,
                 symbol_id=None,
                 at_bid_or_ask=None,
                 unbundled_trade_indicator=None,
                 sale_condition=None,
                 reserve_1=None,
                 reserve_2=None,
                 price=None,
                 volume=None,
                 reserve_3=None,
                 date_time=None):
        self.Type = MessageTypes.MARKET_DATA_UPDATE_TRADE_WITH_UNBUNDLED_INDICATOR
        self.SymbolID = symbol_id
        self.AtBidOrAsk = at_bid_or_ask
        self.UnbundledTradeIndicator = unbundled_trade_indicator
        self.SaleCondition = sale_condition
        self.Reserve_1 = reserve_1
        self.Reserve_2 = reserve_2
        self.Price = price
        self.Volume = volume
        self.Reserve_3 = reserve_3
        self.DateTime = date_time

    @staticmethod
    def from_message_short(message_obj):
        packet = message_obj.get('F')
        return MarketDataUpdateTradeWithUnbundledIndicator(
             symbol_id=packet[0],
             at_bid_or_ask=packet[1],
             unbundled_trade_indicator=packet[2],
             sale_condition=packet[3],
             reserve_1=packet[4],
             reserve_2=packet[5],
             price=packet[6],
             volume=packet[7],
             reserve_3=packet[8],
             date_time=packet[9]
        )

    @staticmethod
    def from_message_long(message_obj):
        return MarketDataUpdateTradeWithUnbundledIndicator(
             symbol_id=message_obj.get('SymbolID'),
             at_bid_or_ask=message_obj.get('AtBidOrAsk'),
             unbundled_trade_indicator=message_obj.get('UnbundledTradeIndicator'),
             sale_condition=message_obj.get('SaleCondition'),
             reserve_1=message_obj.get('Reserve_1'),
             reserve_2=message_obj.get('Reserve_2'),
             price=message_obj.get('Price'),
             volume=message_obj.get('Volume'),
             reserve_3=message_obj.get('Reserve_3'),
             date_time=message_obj.get('DateTime')
        )

    @staticmethod
    def from_message(message_obj):
        if 'F' in message_obj:
            return MarketDataUpdateTradeWithUnbundledIndicator.from_message_short(message_obj)
        else:
            return MarketDataUpdateTradeWithUnbundledIndicator.from_message_long(message_obj)

    @staticmethod
    def get_message_type_name():
        return "MarketDataUpdateTradeWithUnbundledIndicator"
