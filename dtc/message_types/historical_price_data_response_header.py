
import json
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class HistoricalPriceDataResponseHeader(BaseMessageType):
    def __init__(self,
                 request_id=None,
                 record_interval=None,
                 use_z_lib_compression=None,
                 no_records_to_return=None,
                 int_to_float_price_divisor=None):
        self.Type = MessageTypes.HISTORICAL_PRICE_DATA_RESPONSE_HEADER
        self.RequestID = request_id
        self.RecordInterval = record_interval
        self.UseZLibCompression = use_z_lib_compression
        self.NoRecordsToReturn = no_records_to_return
        self.IntToFloatPriceDivisor = int_to_float_price_divisor

