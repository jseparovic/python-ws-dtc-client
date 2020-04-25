
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class HistoricalPriceDataResponseTrailer(BaseMessageType):
    def __init__(self,
                 request_id=None,
                 final_record_last_date_time=None):
        self.Type = MessageTypes.HISTORICAL_PRICE_DATA_RESPONSE_TRAILER
        self.RequestID = request_id
        self.FinalRecordLastDateTime = final_record_last_date_time

    @staticmethod
    def from_message(message_obj):
        return HistoricalPriceDataResponseTrailer(
             request_id=message_obj.get('RequestID'),
             final_record_last_date_time=message_obj.get('FinalRecordLastDateTime')
        )

    @staticmethod
    def get_message_type_name():
        return "HistoricalPriceDataResponseTrailer"
