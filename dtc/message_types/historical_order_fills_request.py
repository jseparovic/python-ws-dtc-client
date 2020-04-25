
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

    @staticmethod
    def from_message_short(message_obj):
        packet = message_obj.get('F')
        return HistoricalOrderFillsRequest(
             request_id=packet[0],
             server_order_id=packet[1],
             number_of_days=packet[2],
             trade_account=packet[3],
             start_date_time=packet[4]
        )

    @staticmethod
    def from_message_long(message_obj):
        return HistoricalOrderFillsRequest(
             request_id=message_obj.get('RequestID'),
             server_order_id=message_obj.get('ServerOrderID'),
             number_of_days=message_obj.get('NumberOfDays'),
             trade_account=message_obj.get('TradeAccount'),
             start_date_time=message_obj.get('StartDateTime')
        )

    @staticmethod
    def from_message(message_obj):
        if 'F' in message_obj:
            return HistoricalOrderFillsRequest.from_message_short(message_obj)
        else:
            return HistoricalOrderFillsRequest.from_message_long(message_obj)

    @staticmethod
    def get_message_type_name():
        return "HistoricalOrderFillsRequest"
