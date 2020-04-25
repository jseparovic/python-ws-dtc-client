import json
import logging
from dtc.enums.message_types import MessageTypes

from dtc.message_types.encoding_request import EncodingRequest
from dtc.message_types.encoding_response import EncodingResponse
from dtc.message_types.logon_request import LogonRequest
from dtc.message_types.logon_response import LogonResponse
from dtc.message_types.logoff import Logoff
from dtc.message_types.heartbeat import Heartbeat
from dtc.message_types.market_data_feed_status import MarketDataFeedStatus
from dtc.message_types.market_data_feed_symbol_status import MarketDataFeedSymbolStatus
from dtc.message_types.trading_symbol_status import TradingSymbolStatus
from dtc.message_types.market_data_request import MarketDataRequest
from dtc.message_types.market_depth_request import MarketDepthRequest
from dtc.message_types.market_data_reject import MarketDataReject
from dtc.message_types.market_data_snapshot import MarketDataSnapshot
from dtc.message_types.market_data_snapshot_int import MarketDataSnapshotInt
from dtc.message_types.market_depth_snapshot_level import MarketDepthSnapshotLevel
from dtc.message_types.market_depth_snapshot_level_float import MarketDepthSnapshotLevelFloat
from dtc.message_types.market_depth_snapshot_level_int import MarketDepthSnapshotLevelInt
from dtc.message_types.market_depth_update_level import MarketDepthUpdateLevel
from dtc.message_types.market_depth_update_level_int import MarketDepthUpdateLevelInt
from dtc.message_types.market_depth_update_level_float_with_milliseconds import MarketDepthUpdateLevelFloatWithMilliseconds
from dtc.message_types.market_depth_update_level_no_timestamp import MarketDepthUpdateLevelNoTimestamp
from dtc.message_types.market_data_update_trade_no_timestamp import MarketDataUpdateTradeNoTimestamp
from dtc.message_types.market_data_update_session_settlement import MarketDataUpdateSessionSettlement
from dtc.message_types.market_data_update_session_settlement_int import MarketDataUpdateSessionSettlementInt
from dtc.message_types.market_data_update_session_open import MarketDataUpdateSessionOpen
from dtc.message_types.market_data_update_session_open_int import MarketDataUpdateSessionOpenInt
from dtc.message_types.market_data_update_session_num_trades import MarketDataUpdateSessionNumTrades
from dtc.message_types.market_data_update_trading_session_date import MarketDataUpdateTradingSessionDate
from dtc.message_types.market_depth_reject import MarketDepthReject
from dtc.message_types.market_data_update_trade import MarketDataUpdateTrade
from dtc.message_types.market_data_update_trade_int import MarketDataUpdateTradeInt
from dtc.message_types.market_data_update_trade_with_unbundled_indicator import MarketDataUpdateTradeWithUnbundledIndicator
from dtc.message_types.market_data_update_bid_ask import MarketDataUpdateBidAsk
from dtc.message_types.market_data_update_bid_ask_int import MarketDataUpdateBidAskInt
from dtc.message_types.market_data_update_bid_ask_compact import MarketDataUpdateBidAskCompact
from dtc.message_types.market_data_update_bid_ask_float_with_milliseconds import MarketDataUpdateBidAskFloatWithMilliseconds
from dtc.message_types.market_data_update_trade_compact import MarketDataUpdateTradeCompact
from dtc.message_types.market_data_update_session_volume import MarketDataUpdateSessionVolume
from dtc.message_types.market_data_update_open_interest import MarketDataUpdateOpenInterest
from dtc.message_types.market_data_update_session_high import MarketDataUpdateSessionHigh
from dtc.message_types.market_data_update_session_high_int import MarketDataUpdateSessionHighInt
from dtc.message_types.market_data_update_session_low import MarketDataUpdateSessionLow
from dtc.message_types.market_data_update_session_low_int import MarketDataUpdateSessionLowInt
from dtc.message_types.market_data_update_last_trade_snapshot import MarketDataUpdateLastTradeSnapshot
from dtc.message_types.submit_new_single_order import SubmitNewSingleOrder
from dtc.message_types.submit_new_single_order_int import SubmitNewSingleOrderInt
from dtc.message_types.submit_flatten_position_order import SubmitFlattenPositionOrder
from dtc.message_types.cancel_replace_order import CancelReplaceOrder
from dtc.message_types.cancel_replace_order_int import CancelReplaceOrderInt
from dtc.message_types.cancel_order import CancelOrder
from dtc.message_types.submit_new_oco_order import SubmitNewOCOOrder
from dtc.message_types.submit_new_oco_order_int import SubmitNewOCOOrderInt
from dtc.message_types.open_orders_request import OpenOrdersRequest
from dtc.message_types.historical_order_fills_request import HistoricalOrderFillsRequest
from dtc.message_types.historical_order_fills_reject import HistoricalOrderFillsReject
from dtc.message_types.current_positions_request import CurrentPositionsRequest
from dtc.message_types.current_positions_reject import CurrentPositionsReject
from dtc.message_types.order_update import OrderUpdate
from dtc.message_types.open_orders_reject import OpenOrdersReject
from dtc.message_types.historical_order_fill_response import HistoricalOrderFillResponse
from dtc.message_types.position_update import PositionUpdate
from dtc.message_types.trade_accounts_request import TradeAccountsRequest
from dtc.message_types.trade_account_response import TradeAccountResponse
from dtc.message_types.exchange_list_request import ExchangeListRequest
from dtc.message_types.exchange_list_response import ExchangeListResponse
from dtc.message_types.symbols_for_exchange_request import SymbolsForExchangeRequest
from dtc.message_types.underlying_symbols_for_exchange_request import UnderlyingSymbolsForExchangeRequest
from dtc.message_types.symbols_for_underlying_request import SymbolsForUnderlyingRequest
from dtc.message_types.symbol_search_request import SymbolSearchRequest
from dtc.message_types.security_definition_for_symbol_request import SecurityDefinitionForSymbolRequest
from dtc.message_types.security_definition_response import SecurityDefinitionResponse
from dtc.message_types.security_definition_reject import SecurityDefinitionReject
from dtc.message_types.account_balance_request import AccountBalanceRequest
from dtc.message_types.account_balance_reject import AccountBalanceReject
from dtc.message_types.account_balance_update import AccountBalanceUpdate
from dtc.message_types.account_balance_adjustment import AccountBalanceAdjustment
from dtc.message_types.account_balance_adjustment_reject import AccountBalanceAdjustmentReject
from dtc.message_types.account_balance_adjustment_complete import AccountBalanceAdjustmentComplete
from dtc.message_types.historical_account_balances_request import HistoricalAccountBalancesRequest
from dtc.message_types.historical_account_balances_reject import HistoricalAccountBalancesReject
from dtc.message_types.historical_account_balance_response import HistoricalAccountBalanceResponse
from dtc.message_types.user_message import UserMessage
from dtc.message_types.general_log_message import GeneralLogMessage
from dtc.message_types.alert_message import AlertMessage
from dtc.message_types.journal_entry_add import JournalEntryAdd
from dtc.message_types.journal_entries_request import JournalEntriesRequest
from dtc.message_types.journal_entries_reject import JournalEntriesReject
from dtc.message_types.journal_entry_response import JournalEntryResponse
from dtc.message_types.historical_price_data_request import HistoricalPriceDataRequest
from dtc.message_types.historical_price_data_response_header import HistoricalPriceDataResponseHeader
from dtc.message_types.historical_price_data_reject import HistoricalPriceDataReject
from dtc.message_types.historical_price_data_record_response import HistoricalPriceDataRecordResponse
from dtc.message_types.historical_price_data_tick_record_response import HistoricalPriceDataTickRecordResponse
from dtc.message_types.historical_price_data_record_response_int import HistoricalPriceDataRecordResponseInt
from dtc.message_types.historical_price_data_tick_record_response_int import HistoricalPriceDataTickRecordResponseInt
from dtc.message_types.historical_price_data_response_trailer import HistoricalPriceDataResponseTrailer

TYPE = 'Type'


class MessageUtil:
    def __init__(self):
        pass

    @staticmethod
    def parse_incoming_message(message_text):
        response = None
        message_obj = json.loads(message_text)

        if message_obj[TYPE] == MessageTypes.ENCODING_REQUEST:
            response = EncodingRequest.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.ENCODING_RESPONSE:
            response = EncodingResponse.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.LOGON_REQUEST:
            response = LogonRequest.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.LOGON_RESPONSE:
            response = LogonResponse.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.LOGOFF:
            response = Logoff.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.HEARTBEAT:
            response = Heartbeat.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.MARKET_DATA_FEED_STATUS:
            response = MarketDataFeedStatus.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.MARKET_DATA_FEED_SYMBOL_STATUS:
            response = MarketDataFeedSymbolStatus.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.TRADING_SYMBOL_STATUS:
            response = TradingSymbolStatus.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.MARKET_DATA_REQUEST:
            response = MarketDataRequest.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.MARKET_DEPTH_REQUEST:
            response = MarketDepthRequest.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.MARKET_DATA_REJECT:
            response = MarketDataReject.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.MARKET_DATA_SNAPSHOT:
            response = MarketDataSnapshot.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.MARKET_DATA_SNAPSHOT_INT:
            response = MarketDataSnapshotInt.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.MARKET_DEPTH_SNAPSHOT_LEVEL:
            response = MarketDepthSnapshotLevel.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.MARKET_DEPTH_SNAPSHOT_LEVEL_FLOAT:
            response = MarketDepthSnapshotLevelFloat.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.MARKET_DEPTH_SNAPSHOT_LEVEL_INT:
            response = MarketDepthSnapshotLevelInt.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.MARKET_DEPTH_UPDATE_LEVEL:
            response = MarketDepthUpdateLevel.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.MARKET_DEPTH_UPDATE_LEVEL_INT:
            response = MarketDepthUpdateLevelInt.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.MARKET_DEPTH_UPDATE_LEVEL_FLOAT_WITH_MILLISECONDS:
            response = MarketDepthUpdateLevelFloatWithMilliseconds.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.MARKET_DEPTH_UPDATE_LEVEL_NO_TIMESTAMP:
            response = MarketDepthUpdateLevelNoTimestamp.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.MARKET_DATA_UPDATE_TRADE_NO_TIMESTAMP:
            response = MarketDataUpdateTradeNoTimestamp.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.MARKET_DATA_UPDATE_SESSION_SETTLEMENT:
            response = MarketDataUpdateSessionSettlement.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.MARKET_DATA_UPDATE_SESSION_SETTLEMENT_INT:
            response = MarketDataUpdateSessionSettlementInt.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.MARKET_DATA_UPDATE_SESSION_OPEN:
            response = MarketDataUpdateSessionOpen.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.MARKET_DATA_UPDATE_SESSION_OPEN_INT:
            response = MarketDataUpdateSessionOpenInt.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.MARKET_DATA_UPDATE_SESSION_NUM_TRADES:
            response = MarketDataUpdateSessionNumTrades.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.MARKET_DATA_UPDATE_TRADING_SESSION_DATE:
            response = MarketDataUpdateTradingSessionDate.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.MARKET_DEPTH_REJECT:
            response = MarketDepthReject.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.MARKET_DATA_UPDATE_TRADE:
            response = MarketDataUpdateTrade.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.MARKET_DATA_UPDATE_TRADE_INT:
            response = MarketDataUpdateTradeInt.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.MARKET_DATA_UPDATE_TRADE_WITH_UNBUNDLED_INDICATOR:
            response = MarketDataUpdateTradeWithUnbundledIndicator.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.MARKET_DATA_UPDATE_BID_ASK:
            response = MarketDataUpdateBidAsk.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.MARKET_DATA_UPDATE_BID_ASK_INT:
            response = MarketDataUpdateBidAskInt.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.MARKET_DATA_UPDATE_BID_ASK_COMPACT:
            response = MarketDataUpdateBidAskCompact.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.MARKET_DATA_UPDATE_BID_ASK_FLOAT_WITH_MILLISECONDS:
            response = MarketDataUpdateBidAskFloatWithMilliseconds.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.MARKET_DATA_UPDATE_TRADE_COMPACT:
            response = MarketDataUpdateTradeCompact.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.MARKET_DATA_UPDATE_SESSION_VOLUME:
            response = MarketDataUpdateSessionVolume.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.MARKET_DATA_UPDATE_OPEN_INTEREST:
            response = MarketDataUpdateOpenInterest.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.MARKET_DATA_UPDATE_SESSION_HIGH:
            response = MarketDataUpdateSessionHigh.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.MARKET_DATA_UPDATE_SESSION_HIGH_INT:
            response = MarketDataUpdateSessionHighInt.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.MARKET_DATA_UPDATE_SESSION_LOW:
            response = MarketDataUpdateSessionLow.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.MARKET_DATA_UPDATE_SESSION_LOW_INT:
            response = MarketDataUpdateSessionLowInt.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.MARKET_DATA_UPDATE_LAST_TRADE_SNAPSHOT:
            response = MarketDataUpdateLastTradeSnapshot.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.SUBMIT_NEW_SINGLE_ORDER:
            response = SubmitNewSingleOrder.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.SUBMIT_NEW_SINGLE_ORDER_INT:
            response = SubmitNewSingleOrderInt.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.SUBMIT_FLATTEN_POSITION_ORDER:
            response = SubmitFlattenPositionOrder.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.CANCEL_REPLACE_ORDER:
            response = CancelReplaceOrder.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.CANCEL_REPLACE_ORDER_INT:
            response = CancelReplaceOrderInt.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.CANCEL_ORDER:
            response = CancelOrder.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.SUBMIT_NEW_OCO_ORDER:
            response = SubmitNewOCOOrder.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.SUBMIT_NEW_OCO_ORDER_INT:
            response = SubmitNewOCOOrderInt.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.OPEN_ORDERS_REQUEST:
            response = OpenOrdersRequest.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.HISTORICAL_ORDER_FILLS_REQUEST:
            response = HistoricalOrderFillsRequest.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.HISTORICAL_ORDER_FILLS_REJECT:
            response = HistoricalOrderFillsReject.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.CURRENT_POSITIONS_REQUEST:
            response = CurrentPositionsRequest.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.CURRENT_POSITIONS_REJECT:
            response = CurrentPositionsReject.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.ORDER_UPDATE:
            response = OrderUpdate.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.OPEN_ORDERS_REJECT:
            response = OpenOrdersReject.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.HISTORICAL_ORDER_FILL_RESPONSE:
            response = HistoricalOrderFillResponse.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.POSITION_UPDATE:
            response = PositionUpdate.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.TRADE_ACCOUNTS_REQUEST:
            response = TradeAccountsRequest.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.TRADE_ACCOUNT_RESPONSE:
            response = TradeAccountResponse.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.EXCHANGE_LIST_REQUEST:
            response = ExchangeListRequest.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.EXCHANGE_LIST_RESPONSE:
            response = ExchangeListResponse.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.SYMBOLS_FOR_EXCHANGE_REQUEST:
            response = SymbolsForExchangeRequest.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.UNDERLYING_SYMBOLS_FOR_EXCHANGE_REQUEST:
            response = UnderlyingSymbolsForExchangeRequest.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.SYMBOLS_FOR_UNDERLYING_REQUEST:
            response = SymbolsForUnderlyingRequest.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.SYMBOL_SEARCH_REQUEST:
            response = SymbolSearchRequest.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.SECURITY_DEFINITION_FOR_SYMBOL_REQUEST:
            response = SecurityDefinitionForSymbolRequest.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.SECURITY_DEFINITION_RESPONSE:
            response = SecurityDefinitionResponse.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.SECURITY_DEFINITION_REJECT:
            response = SecurityDefinitionReject.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.ACCOUNT_BALANCE_REQUEST:
            response = AccountBalanceRequest.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.ACCOUNT_BALANCE_REJECT:
            response = AccountBalanceReject.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.ACCOUNT_BALANCE_UPDATE:
            response = AccountBalanceUpdate.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.ACCOUNT_BALANCE_ADJUSTMENT:
            response = AccountBalanceAdjustment.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.ACCOUNT_BALANCE_ADJUSTMENT_REJECT:
            response = AccountBalanceAdjustmentReject.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.ACCOUNT_BALANCE_ADJUSTMENT_COMPLETE:
            response = AccountBalanceAdjustmentComplete.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.HISTORICAL_ACCOUNT_BALANCES_REQUEST:
            response = HistoricalAccountBalancesRequest.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.HISTORICAL_ACCOUNT_BALANCES_REJECT:
            response = HistoricalAccountBalancesReject.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.HISTORICAL_ACCOUNT_BALANCE_RESPONSE:
            response = HistoricalAccountBalanceResponse.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.USER_MESSAGE:
            response = UserMessage.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.GENERAL_LOG_MESSAGE:
            response = GeneralLogMessage.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.ALERT_MESSAGE:
            response = AlertMessage.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.JOURNAL_ENTRY_ADD:
            response = JournalEntryAdd.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.JOURNAL_ENTRIES_REQUEST:
            response = JournalEntriesRequest.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.JOURNAL_ENTRIES_REJECT:
            response = JournalEntriesReject.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.JOURNAL_ENTRY_RESPONSE:
            response = JournalEntryResponse.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.HISTORICAL_PRICE_DATA_REQUEST:
            response = HistoricalPriceDataRequest.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.HISTORICAL_PRICE_DATA_RESPONSE_HEADER:
            response = HistoricalPriceDataResponseHeader.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.HISTORICAL_PRICE_DATA_REJECT:
            response = HistoricalPriceDataReject.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.HISTORICAL_PRICE_DATA_RECORD_RESPONSE:
            response = HistoricalPriceDataRecordResponse.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.HISTORICAL_PRICE_DATA_TICK_RECORD_RESPONSE:
            response = HistoricalPriceDataTickRecordResponse.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.HISTORICAL_PRICE_DATA_RECORD_RESPONSE_INT:
            response = HistoricalPriceDataRecordResponseInt.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.HISTORICAL_PRICE_DATA_TICK_RECORD_RESPONSE_INT:
            response = HistoricalPriceDataTickRecordResponseInt.from_message(message_obj)
        elif message_obj[TYPE] == MessageTypes.HISTORICAL_PRICE_DATA_RESPONSE_TRAILER:
            response = HistoricalPriceDataResponseTrailer.from_message(message_obj)

        return response
