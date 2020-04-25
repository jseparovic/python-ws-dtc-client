
import json
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class SubmitFlattenPositionOrder(BaseMessageType):
    def __init__(self,
                 symbol=None,
                 exchange=None,
                 trade_account=None,
                 client_order_id=None,
                 free_form_text=None,
                 is_automated_order=None):
        self.Type = MessageTypes.SUBMIT_FLATTEN_POSITION_ORDER
        self.Symbol = symbol
        self.Exchange = exchange
        self.TradeAccount = trade_account
        self.ClientOrderID = client_order_id
        self.FreeFormText = free_form_text
        self.IsAutomatedOrder = is_automated_order

