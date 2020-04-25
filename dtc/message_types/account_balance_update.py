
import json
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class AccountBalanceUpdate(BaseMessageType):
    def __init__(self,
                 request_id=None,
                 cash_balance=None,
                 balance_available_for_new_positions=None,
                 account_currency=None,
                 trade_account=None,
                 securities_value=None,
                 margin_requirement=None,
                 total_number_messages=None,
                 message_number=None,
                 no_account_balances=None,
                 unsolicited=None,
                 open_positions_profit_loss=None,
                 daily_profit_loss=None,
                 info_text=None,
                 transaction_identifier=None):
        self.Type = MessageTypes.ACCOUNT_BALANCE_UPDATE
        self.RequestID = request_id
        self.CashBalance = cash_balance
        self.BalanceAvailableForNewPositions = balance_available_for_new_positions
        self.AccountCurrency = account_currency
        self.TradeAccount = trade_account
        self.SecuritiesValue = securities_value
        self.MarginRequirement = margin_requirement
        self.TotalNumberMessages = total_number_messages
        self.MessageNumber = message_number
        self.NoAccountBalances = no_account_balances
        self.Unsolicited = unsolicited
        self.OpenPositionsProfitLoss = open_positions_profit_loss
        self.DailyProfitLoss = daily_profit_loss
        self.InfoText = info_text
        self.TransactionIdentifier = transaction_identifier

