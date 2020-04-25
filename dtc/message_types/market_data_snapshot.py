
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class MarketDataSnapshot(BaseMessageType):
    def __init__(self,
                 symbol_id=None,
                 session_settlement_price=None,
                 session_open_price=None,
                 session_high_price=None,
                 session_low_price=None,
                 session_volume=None,
                 session_num_trades=None,
                 open_interest=None,
                 bid_price=None,
                 ask_price=None,
                 ask_quantity=None,
                 bid_quantity=None,
                 last_trade_price=None,
                 last_trade_volume=None,
                 last_trade_date_time=None,
                 bid_ask_date_time=None,
                 session_settlement_date_time=None,
                 trading_session_date=None,
                 trading_status=None,
                 market_depth_update_date_time=None):
        self.Type = MessageTypes.MARKET_DATA_SNAPSHOT
        self.SymbolID = symbol_id
        self.SessionSettlementPrice = session_settlement_price
        self.SessionOpenPrice = session_open_price
        self.SessionHighPrice = session_high_price
        self.SessionLowPrice = session_low_price
        self.SessionVolume = session_volume
        self.SessionNumTrades = session_num_trades
        self.OpenInterest = open_interest
        self.BidPrice = bid_price
        self.AskPrice = ask_price
        self.AskQuantity = ask_quantity
        self.BidQuantity = bid_quantity
        self.LastTradePrice = last_trade_price
        self.LastTradeVolume = last_trade_volume
        self.LastTradeDateTime = last_trade_date_time
        self.BidAskDateTime = bid_ask_date_time
        self.SessionSettlementDateTime = session_settlement_date_time
        self.TradingSessionDate = trading_session_date
        self.TradingStatus = trading_status
        self.MarketDepthUpdateDateTime = market_depth_update_date_time

    @staticmethod
    def from_message_short(message_obj):
        packet = message_obj.get('F')
        return MarketDataSnapshot(
             symbol_id=packet[0],
             session_settlement_price=packet[1],
             session_open_price=packet[2],
             session_high_price=packet[3],
             session_low_price=packet[4],
             session_volume=packet[5],
             session_num_trades=packet[6],
             open_interest=packet[7],
             bid_price=packet[8],
             ask_price=packet[9],
             ask_quantity=packet[10],
             bid_quantity=packet[11],
             last_trade_price=packet[12],
             last_trade_volume=packet[13],
             last_trade_date_time=packet[14],
             bid_ask_date_time=packet[15],
             session_settlement_date_time=packet[16],
             trading_session_date=packet[17],
             trading_status=packet[18],
             market_depth_update_date_time=packet[19]
        )

    @staticmethod
    def from_message_long(message_obj):
        return MarketDataSnapshot(
             symbol_id=message_obj.get('SymbolID'),
             session_settlement_price=message_obj.get('SessionSettlementPrice'),
             session_open_price=message_obj.get('SessionOpenPrice'),
             session_high_price=message_obj.get('SessionHighPrice'),
             session_low_price=message_obj.get('SessionLowPrice'),
             session_volume=message_obj.get('SessionVolume'),
             session_num_trades=message_obj.get('SessionNumTrades'),
             open_interest=message_obj.get('OpenInterest'),
             bid_price=message_obj.get('BidPrice'),
             ask_price=message_obj.get('AskPrice'),
             ask_quantity=message_obj.get('AskQuantity'),
             bid_quantity=message_obj.get('BidQuantity'),
             last_trade_price=message_obj.get('LastTradePrice'),
             last_trade_volume=message_obj.get('LastTradeVolume'),
             last_trade_date_time=message_obj.get('LastTradeDateTime'),
             bid_ask_date_time=message_obj.get('BidAskDateTime'),
             session_settlement_date_time=message_obj.get('SessionSettlementDateTime'),
             trading_session_date=message_obj.get('TradingSessionDate'),
             trading_status=message_obj.get('TradingStatus'),
             market_depth_update_date_time=message_obj.get('MarketDepthUpdateDateTime')
        )

    @staticmethod
    def from_message(message_obj):
        if 'F' in message_obj:
            return MarketDataSnapshot.from_message_short(message_obj)
        else:
            return MarketDataSnapshot.from_message_long(message_obj)

    @staticmethod
    def get_message_type_name():
        return "MarketDataSnapshot"
