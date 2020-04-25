
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class HistoricalPriceDataTickRecordResponse(BaseMessageType):
    def __init__(self,
                 request_id=None,
                 date_time=None,
                 at_bid_or_ask=None,
                 price=None,
                 volume=None,
                 is_final_record=None):
        self.Type = MessageTypes.HISTORICAL_PRICE_DATA_TICK_RECORD_RESPONSE
        self.RequestID = request_id
        self.DateTime = date_time
        self.AtBidOrAsk = at_bid_or_ask
        self.Price = price
        self.Volume = volume
        self.IsFinalRecord = is_final_record

    @staticmethod
    def from_message(message_obj):
        return HistoricalPriceDataTickRecordResponse(
             request_id=message_obj.get('RequestID'),
             date_time=message_obj.get('DateTime'),
             at_bid_or_ask=message_obj.get('AtBidOrAsk'),
             price=message_obj.get('Price'),
             volume=message_obj.get('Volume'),
             is_final_record=message_obj.get('IsFinalRecord')
        )

    @staticmethod
    def get_message_type_name():
        return "HistoricalPriceDataTickRecordResponse"
