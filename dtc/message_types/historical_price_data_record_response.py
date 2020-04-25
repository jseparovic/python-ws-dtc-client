
import json
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class HistoricalPriceDataRecordResponse(BaseMessageType):
    def __init__(self,
                 request_id=None,
                 start_date_time=None,
                 open_price=None,
                 high_price=None,
                 low_price=None,
                 last_price=None,
                 volume=None,
                 bid_volume=None,
                 ask_volume=None,
                 is_final_record=None):
        self.Type = MessageTypes.HISTORICAL_PRICE_DATA_RECORD_RESPONSE
        self.RequestID = request_id
        self.StartDateTime = start_date_time
        self.OpenPrice = open_price
        self.HighPrice = high_price
        self.LowPrice = low_price
        self.LastPrice = last_price
        self.Volume = volume
        self.BidVolume = bid_volume
        self.AskVolume = ask_volume
        self.IsFinalRecord = is_final_record

