
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class HistoricalPriceDataTickRecordResponseInt(BaseMessageType):
    def __init__(self,
                 request_id=None,
                 date_time=None,
                 price=None,
                 volume=None,
                 at_bid_or_ask=None,
                 is_final_record=None):
        self.Type = MessageTypes.HISTORICAL_PRICE_DATA_TICK_RECORD_RESPONSE_INT
        self.RequestID = request_id
        self.DateTime = date_time
        self.Price = price
        self.Volume = volume
        self.AtBidOrAsk = at_bid_or_ask
        self.IsFinalRecord = is_final_record

    @staticmethod
    def from_message(message_obj):
        return HistoricalPriceDataTickRecordResponseInt(
             request_id=message_obj.get('RequestID'),
             date_time=message_obj.get('DateTime'),
             price=message_obj.get('Price'),
             volume=message_obj.get('Volume'),
             at_bid_or_ask=message_obj.get('AtBidOrAsk'),
             is_final_record=message_obj.get('IsFinalRecord')
        )

    @staticmethod
    def get_message_type_name():
        return "HistoricalPriceDataTickRecordResponseInt"
