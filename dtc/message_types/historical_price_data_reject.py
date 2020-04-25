
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class HistoricalPriceDataReject(BaseMessageType):
    def __init__(self,
                 request_id=None,
                 reject_text=None,
                 reject_reason_code=None,
                 retry_time_in_seconds=None):
        self.Type = MessageTypes.HISTORICAL_PRICE_DATA_REJECT
        self.RequestID = request_id
        self.RejectText = reject_text
        self.RejectReasonCode = reject_reason_code
        self.RetryTimeInSeconds = retry_time_in_seconds

    @staticmethod
    def from_message(message_obj):
        return HistoricalPriceDataReject(
             request_id=message_obj.get('RequestID'),
             reject_text=message_obj.get('RejectText'),
             reject_reason_code=message_obj.get('RejectReasonCode'),
             retry_time_in_seconds=message_obj.get('RetryTimeInSeconds')
        )

    @staticmethod
    def get_message_type_name():
        return "HistoricalPriceDataReject"
