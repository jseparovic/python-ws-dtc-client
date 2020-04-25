
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class TradeAccountsRequest(BaseMessageType):
    def __init__(self,
                 request_id=None):
        self.Type = MessageTypes.TRADE_ACCOUNTS_REQUEST
        self.RequestID = request_id

    @staticmethod
    def from_message(message_obj):
        return TradeAccountsRequest(
             request_id=message_obj.get('RequestID')
        )

    @staticmethod
    def get_message_type_name():
        return "TradeAccountsRequest"
