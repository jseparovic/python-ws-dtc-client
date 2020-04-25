
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class TradeAccountsRequest(BaseMessageType):
    def __init__(self,
                 request_id=None):
        self.Type = MessageTypes.TRADE_ACCOUNTS_REQUEST
        self.RequestID = request_id

    @staticmethod
    def from_message_short(message_obj):
        packet = message_obj.get('F')
        return TradeAccountsRequest(
             request_id=packet[0]
        )

    @staticmethod
    def from_message_long(message_obj):
        return TradeAccountsRequest(
             request_id=message_obj.get('RequestID')
        )

    @staticmethod
    def from_message(message_obj):
        if 'F' in message_obj:
            return TradeAccountsRequest.from_message_short(message_obj)
        else:
            return TradeAccountsRequest.from_message_long(message_obj)

    @staticmethod
    def get_message_type_name():
        return "TradeAccountsRequest"
