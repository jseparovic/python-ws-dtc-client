
import json
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class HistoricalPriceDataRequest(BaseMessageType):
    def __init__(self,
                 request_id=None,
                 symbol=None,
                 exchange=None,
                 record_interval=None,
                 start_date_time=None,
                 end_date_time=None,
                 max_days_to_return=None,
                 use_z_lib_compression=None,
                 request_dividend_adjusted_stock_data=None,
                 flag_1=None):
        self.Type = MessageTypes.HISTORICAL_PRICE_DATA_REQUEST
        self.RequestID = request_id
        self.Symbol = symbol
        self.Exchange = exchange
        self.RecordInterval = record_interval
        self.StartDateTime = start_date_time
        self.EndDateTime = end_date_time
        self.MaxDaysToReturn = max_days_to_return
        self.UseZLibCompression = use_z_lib_compression
        self.RequestDividendAdjustedStockData = request_dividend_adjusted_stock_data
        self.Flag_1 = flag_1

