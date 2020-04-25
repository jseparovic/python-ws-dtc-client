
import json
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

