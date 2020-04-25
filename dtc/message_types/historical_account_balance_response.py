
import json
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

