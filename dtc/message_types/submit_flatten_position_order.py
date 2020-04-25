
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

    @staticmethod
    def from_message(message_obj):
        return SubmitFlattenPositionOrder(
             symbol=message_obj.get('Symbol'),
             exchange=message_obj.get('Exchange'),
             trade_account=message_obj.get('TradeAccount'),
             client_order_id=message_obj.get('ClientOrderID'),
             free_form_text=message_obj.get('FreeFormText'),
             is_automated_order=message_obj.get('IsAutomatedOrder')
        )

    @staticmethod
    def get_message_type_name():
        return "SubmitFlattenPositionOrder"
