
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

    @staticmethod
    def from_message_short(message_obj):
        packet = message_obj.get('F')
        return HistoricalPriceDataRequest(
             request_id=packet[0],
             symbol=packet[1],
             exchange=packet[2],
             record_interval=packet[3],
             start_date_time=packet[4],
             end_date_time=packet[5],
             max_days_to_return=packet[6],
             use_z_lib_compression=packet[7],
             request_dividend_adjusted_stock_data=packet[8],
             flag_1=packet[9]
        )

    @staticmethod
    def from_message_long(message_obj):
        return HistoricalPriceDataRequest(
             request_id=message_obj.get('RequestID'),
             symbol=message_obj.get('Symbol'),
             exchange=message_obj.get('Exchange'),
             record_interval=message_obj.get('RecordInterval'),
             start_date_time=message_obj.get('StartDateTime'),
             end_date_time=message_obj.get('EndDateTime'),
             max_days_to_return=message_obj.get('MaxDaysToReturn'),
             use_z_lib_compression=message_obj.get('UseZLibCompression'),
             request_dividend_adjusted_stock_data=message_obj.get('RequestDividendAdjustedStockData'),
             flag_1=message_obj.get('Flag_1')
        )

    @staticmethod
    def from_message(message_obj):
        if 'F' in message_obj:
            return HistoricalPriceDataRequest.from_message_short(message_obj)
        else:
            return HistoricalPriceDataRequest.from_message_long(message_obj)

    @staticmethod
    def get_message_type_name():
        return "HistoricalPriceDataRequest"
