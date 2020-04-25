
import json
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class TradeAccountsRequest(BaseMessageType):
    def __init__(self,
                 request_id=None):
        self.Type = MessageTypes.TRADE_ACCOUNTS_REQUEST
        self.RequestID = request_id

