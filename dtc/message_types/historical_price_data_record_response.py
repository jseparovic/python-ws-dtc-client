
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

    @staticmethod
    def from_message(message_obj):
        return HistoricalPriceDataRecordResponse(
             request_id=message_obj.get('RequestID'),
             start_date_time=message_obj.get('StartDateTime'),
             open_price=message_obj.get('OpenPrice'),
             high_price=message_obj.get('HighPrice'),
             low_price=message_obj.get('LowPrice'),
             last_price=message_obj.get('LastPrice'),
             volume=message_obj.get('Volume'),
             bid_volume=message_obj.get('BidVolume'),
             ask_volume=message_obj.get('AskVolume'),
             is_final_record=message_obj.get('IsFinalRecord')
        )

    @staticmethod
    def get_message_type_name():
        return "HistoricalPriceDataRecordResponse"
