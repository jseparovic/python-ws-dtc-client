
import json
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class AlertMessage(BaseMessageType):
    def __init__(self,
                 message_text=None,
                 trade_account=None):
        self.Type = MessageTypes.ALERT_MESSAGE
        self.MessageText = message_text
        self.TradeAccount = trade_account

