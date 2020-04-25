
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class HistoricalAccountBalanceResponse(BaseMessageType):
    def __init__(self,
                 request_id=None,
                 date_time=None,
                 cash_balance=None,
                 account_currency=None,
                 trade_account=None,
                 is_final_response=None,
                 no_account_balances=None,
                 info_text=None,
                 transaction_id=None):
        self.Type = MessageTypes.HISTORICAL_ACCOUNT_BALANCE_RESPONSE
        self.RequestID = request_id
        self.DateTime = date_time
        self.CashBalance = cash_balance
        self.AccountCurrency = account_currency
        self.TradeAccount = trade_account
        self.IsFinalResponse = is_final_response
        self.NoAccountBalances = no_account_balances
        self.InfoText = info_text
        self.TransactionId = transaction_id

    @staticmethod
    def from_message(message_obj):
        return HistoricalAccountBalanceResponse(
             request_id=message_obj.get('RequestID'),
             date_time=message_obj.get('DateTime'),
             cash_balance=message_obj.get('CashBalance'),
             account_currency=message_obj.get('AccountCurrency'),
             trade_account=message_obj.get('TradeAccount'),
             is_final_response=message_obj.get('IsFinalResponse'),
             no_account_balances=message_obj.get('NoAccountBalances'),
             info_text=message_obj.get('InfoText'),
             transaction_id=message_obj.get('TransactionId')
        )

    @staticmethod
    def get_message_type_name():
        return "HistoricalAccountBalanceResponse"
