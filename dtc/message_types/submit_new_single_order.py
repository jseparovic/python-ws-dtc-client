
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class SubmitNewSingleOrder(BaseMessageType):
    def __init__(self,
                 symbol=None,
                 exchange=None,
                 trade_account=None,
                 client_order_id=None,
                 order_type=None,
                 buy_sell=None,
                 price1=None,
                 price2=None,
                 quantity=None,
                 time_in_force=None,
                 good_till_date_time=None,
                 is_automated_order=None,
                 is_parent_order=None,
                 free_form_text=None,
                 open_or_close=None,
                 max_show_quantity=None):
        self.Type = MessageTypes.SUBMIT_NEW_SINGLE_ORDER
        self.Symbol = symbol
        self.Exchange = exchange
        self.TradeAccount = trade_account
        self.ClientOrderID = client_order_id
        self.OrderType = order_type
        self.BuySell = buy_sell
        self.Price1 = price1
        self.Price2 = price2
        self.Quantity = quantity
        self.TimeInForce = time_in_force
        self.GoodTillDateTime = good_till_date_time
        self.IsAutomatedOrder = is_automated_order
        self.IsParentOrder = is_parent_order
        self.FreeFormText = free_form_text
        self.OpenOrClose = open_or_close
        self.MaxShowQuantity = max_show_quantity

    @staticmethod
    def from_message(message_obj):
        return SubmitNewSingleOrder(
             symbol=message_obj.get('Symbol'),
             exchange=message_obj.get('Exchange'),
             trade_account=message_obj.get('TradeAccount'),
             client_order_id=message_obj.get('ClientOrderID'),
             order_type=message_obj.get('OrderType'),
             buy_sell=message_obj.get('BuySell'),
             price1=message_obj.get('Price1'),
             price2=message_obj.get('Price2'),
             quantity=message_obj.get('Quantity'),
             time_in_force=message_obj.get('TimeInForce'),
             good_till_date_time=message_obj.get('GoodTillDateTime'),
             is_automated_order=message_obj.get('IsAutomatedOrder'),
             is_parent_order=message_obj.get('IsParentOrder'),
             free_form_text=message_obj.get('FreeFormText'),
             open_or_close=message_obj.get('OpenOrClose'),
             max_show_quantity=message_obj.get('MaxShowQuantity')
        )

    @staticmethod
    def get_message_type_name():
        return "SubmitNewSingleOrder"
