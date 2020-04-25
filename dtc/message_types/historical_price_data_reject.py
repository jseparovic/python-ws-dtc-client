
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
    def from_message_short(message_obj):
        packet = message_obj.get('F')
        return HistoricalPriceDataReject(
             request_id=packet[0],
             reject_text=packet[1],
             reject_reason_code=packet[2],
             retry_time_in_seconds=packet[3]
        )

    @staticmethod
    def from_message_long(message_obj):
        return HistoricalPriceDataReject(
             request_id=message_obj.get('RequestID'),
             reject_text=message_obj.get('RejectText'),
             reject_reason_code=message_obj.get('RejectReasonCode'),
             retry_time_in_seconds=message_obj.get('RetryTimeInSeconds')
        )

    @staticmethod
    def from_message(message_obj):
        if 'F' in message_obj:
            return HistoricalPriceDataReject.from_message_short(message_obj)
        else:
            return HistoricalPriceDataReject.from_message_long(message_obj)

    @staticmethod
    def get_message_type_name():
        return "HistoricalPriceDataReject"
