
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

    @staticmethod
    def from_message_short(message_obj):
        packet = message_obj.get('F')
        return AccountBalanceUpdate(
             request_id=packet[0],
             cash_balance=packet[1],
             balance_available_for_new_positions=packet[2],
             account_currency=packet[3],
             trade_account=packet[4],
             securities_value=packet[5],
             margin_requirement=packet[6],
             total_number_messages=packet[7],
             message_number=packet[8],
             no_account_balances=packet[9],
             unsolicited=packet[10],
             open_positions_profit_loss=packet[11],
             daily_profit_loss=packet[12],
             info_text=packet[13],
             transaction_identifier=packet[14]
        )

    @staticmethod
    def from_message_long(message_obj):
        return AccountBalanceUpdate(
             request_id=message_obj.get('RequestID'),
             cash_balance=message_obj.get('CashBalance'),
             balance_available_for_new_positions=message_obj.get('BalanceAvailableForNewPositions'),
             account_currency=message_obj.get('AccountCurrency'),
             trade_account=message_obj.get('TradeAccount'),
             securities_value=message_obj.get('SecuritiesValue'),
             margin_requirement=message_obj.get('MarginRequirement'),
             total_number_messages=message_obj.get('TotalNumberMessages'),
             message_number=message_obj.get('MessageNumber'),
             no_account_balances=message_obj.get('NoAccountBalances'),
             unsolicited=message_obj.get('Unsolicited'),
             open_positions_profit_loss=message_obj.get('OpenPositionsProfitLoss'),
             daily_profit_loss=message_obj.get('DailyProfitLoss'),
             info_text=message_obj.get('InfoText'),
             transaction_identifier=message_obj.get('TransactionIdentifier')
        )

    @staticmethod
    def from_message(message_obj):
        if 'F' in message_obj:
            return AccountBalanceUpdate.from_message_short(message_obj)
        else:
            return AccountBalanceUpdate.from_message_long(message_obj)

    @staticmethod
    def get_message_type_name():
        return "AccountBalanceUpdate"
