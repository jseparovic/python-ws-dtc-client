
import json
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

