
import json
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class TradeAccountResponse(BaseMessageType):
    def __init__(self,
                 total_number_messages=None,
                 message_number=None,
                 trade_account=None,
                 request_id=None):
        self.Type = MessageTypes.TRADE_ACCOUNT_RESPONSE
        self.TotalNumberMessages = total_number_messages
        self.MessageNumber = message_number
        self.TradeAccount = trade_account
        self.RequestID = request_id

