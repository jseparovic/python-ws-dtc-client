
import json
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class ExchangeListResponse(BaseMessageType):
    def __init__(self,
                 request_id=None,
                 exchange=None,
                 is_final_message=None,
                 description=None):
        self.Type = MessageTypes.EXCHANGE_LIST_RESPONSE
        self.RequestID = request_id
        self.Exchange = exchange
        self.IsFinalMessage = is_final_message
        self.Description = description

