
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class AccountBalanceAdjustmentComplete(BaseMessageType):
    def __init__(self,
                 request_id=None,
                 transaction_id=None):
        self.Type = MessageTypes.ACCOUNT_BALANCE_ADJUSTMENT_COMPLETE
        self.RequestID = request_id
        self.TransactionID = transaction_id

    @staticmethod
    def from_message(message_obj):
        return AccountBalanceAdjustmentComplete(
             request_id=message_obj.get('RequestID'),
             transaction_id=message_obj.get('TransactionID')
        )

    @staticmethod
    def get_message_type_name():
        return "AccountBalanceAdjustmentComplete"
