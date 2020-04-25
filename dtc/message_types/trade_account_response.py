
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class TradeAccountResponse(BaseMessageType):
    def __init__(self,
                 total_number_messages=None,
                 message_number=None,
                 trade_account=None,
                 request_id=None):
        self.Type = MessageTypes.TRADE_ACCOUNT_RESPONSE
        self.TotalNumberMessages = total_number_messages
        self.MessageNumber = message_number
        self.TradeAccount = trade_account
        self.RequestID = request_id

    @staticmethod
    def from_message_short(message_obj):
        packet = message_obj.get('F')
        return TradeAccountResponse(
             total_number_messages=packet[0],
             message_number=packet[1],
             trade_account=packet[2],
             request_id=packet[3]
        )

    @staticmethod
    def from_message_long(message_obj):
        return TradeAccountResponse(
             total_number_messages=message_obj.get('TotalNumberMessages'),
             message_number=message_obj.get('MessageNumber'),
             trade_account=message_obj.get('TradeAccount'),
             request_id=message_obj.get('RequestID')
        )

    @staticmethod
    def from_message(message_obj):
        if 'F' in message_obj:
            return TradeAccountResponse.from_message_short(message_obj)
        else:
            return TradeAccountResponse.from_message_long(message_obj)

    @staticmethod
    def get_message_type_name():
        return "TradeAccountResponse"
