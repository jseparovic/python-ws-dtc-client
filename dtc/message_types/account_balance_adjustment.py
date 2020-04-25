
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class AccountBalanceAdjustment(BaseMessageType):
    def __init__(self,
                 request_id=None,
                 trade_account=None,
                 credit_amount=None,
                 debit_amount=None,
                 currency=None,
                 reason=None):
        self.Type = MessageTypes.ACCOUNT_BALANCE_ADJUSTMENT
        self.RequestID = request_id
        self.TradeAccount = trade_account
        self.CreditAmount = credit_amount
        self.DebitAmount = debit_amount
        self.Currency = currency
        self.Reason = reason

    @staticmethod
    def from_message_short(message_obj):
        packet = message_obj.get('F')
        return AccountBalanceAdjustment(
             request_id=packet[0],
             trade_account=packet[1],
             credit_amount=packet[2],
             debit_amount=packet[3],
             currency=packet[4],
             reason=packet[5]
        )

    @staticmethod
    def from_message_long(message_obj):
        return AccountBalanceAdjustment(
             request_id=message_obj.get('RequestID'),
             trade_account=message_obj.get('TradeAccount'),
             credit_amount=message_obj.get('CreditAmount'),
             debit_amount=message_obj.get('DebitAmount'),
             currency=message_obj.get('Currency'),
             reason=message_obj.get('Reason')
        )

    @staticmethod
    def from_message(message_obj):
        if 'F' in message_obj:
            return AccountBalanceAdjustment.from_message_short(message_obj)
        else:
            return AccountBalanceAdjustment.from_message_long(message_obj)

    @staticmethod
    def get_message_type_name():
        return "AccountBalanceAdjustment"
