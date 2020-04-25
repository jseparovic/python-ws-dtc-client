
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class HistoricalAccountBalancesRequest(BaseMessageType):
    def __init__(self,
                 request_id=None,
                 trade_account=None,
                 start_date_time=None):
        self.Type = MessageTypes.HISTORICAL_ACCOUNT_BALANCES_REQUEST
        self.RequestID = request_id
        self.TradeAccount = trade_account
        self.StartDateTime = start_date_time

    @staticmethod
    def from_message_short(message_obj):
        packet = message_obj.get('F')
        return HistoricalAccountBalancesRequest(
             request_id=packet[0],
             trade_account=packet[1],
             start_date_time=packet[2]
        )

    @staticmethod
    def from_message_long(message_obj):
        return HistoricalAccountBalancesRequest(
             request_id=message_obj.get('RequestID'),
             trade_account=message_obj.get('TradeAccount'),
             start_date_time=message_obj.get('StartDateTime')
        )

    @staticmethod
    def from_message(message_obj):
        if 'F' in message_obj:
            return HistoricalAccountBalancesRequest.from_message_short(message_obj)
        else:
            return HistoricalAccountBalancesRequest.from_message_long(message_obj)

    @staticmethod
    def get_message_type_name():
        return "HistoricalAccountBalancesRequest"
