
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class HistoricalPriceDataRecordResponseInt(BaseMessageType):
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
        self.Type = MessageTypes.HISTORICAL_PRICE_DATA_RECORD_RESPONSE_INT
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
    def from_message_short(message_obj):
        packet = message_obj.get('F')
        return HistoricalPriceDataRecordResponseInt(
             request_id=packet[0],
             start_date_time=packet[1],
             open_price=packet[2],
             high_price=packet[3],
             low_price=packet[4],
             last_price=packet[5],
             volume=packet[6],
             bid_volume=packet[7],
             ask_volume=packet[8],
             is_final_record=packet[9]
        )

    @staticmethod
    def from_message_long(message_obj):
        return HistoricalPriceDataRecordResponseInt(
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
    def from_message(message_obj):
        if 'F' in message_obj:
            return HistoricalPriceDataRecordResponseInt.from_message_short(message_obj)
        else:
            return HistoricalPriceDataRecordResponseInt.from_message_long(message_obj)

    @staticmethod
    def get_message_type_name():
        return "HistoricalPriceDataRecordResponseInt"
