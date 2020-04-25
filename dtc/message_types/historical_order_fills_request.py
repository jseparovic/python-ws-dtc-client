
import json
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class HistoricalOrderFillsRequest(BaseMessageType):
    def __init__(self,
                 request_id=None,
                 server_order_id=None,
                 number_of_days=None,
                 trade_account=None,
                 start_date_time=None):
        self.Type = MessageTypes.HISTORICAL_ORDER_FILLS_REQUEST
        self.RequestID = request_id
        self.ServerOrderID = server_order_id
        self.NumberOfDays = number_of_days
        self.TradeAccount = trade_account
        self.StartDateTime = start_date_time

