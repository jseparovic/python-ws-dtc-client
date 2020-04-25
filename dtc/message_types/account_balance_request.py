
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class AccountBalanceRequest(BaseMessageType):
    def __init__(self,
                 request_id=None,
                 trade_account=None):
        self.Type = MessageTypes.ACCOUNT_BALANCE_REQUEST
        self.RequestID = request_id
        self.TradeAccount = trade_account

    @staticmethod
    def from_message_short(message_obj):
        packet = message_obj.get('F')
        return AccountBalanceRequest(
             request_id=packet[0],
             trade_account=packet[1]
        )

    @staticmethod
    def from_message_long(message_obj):
        return AccountBalanceRequest(
             request_id=message_obj.get('RequestID'),
             trade_account=message_obj.get('TradeAccount')
        )

    @staticmethod
    def from_message(message_obj):
        if 'F' in message_obj:
            return AccountBalanceRequest.from_message_short(message_obj)
        else:
            return AccountBalanceRequest.from_message_long(message_obj)

    @staticmethod
    def get_message_type_name():
        return "AccountBalanceRequest"
