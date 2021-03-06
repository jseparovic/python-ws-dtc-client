
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class SubmitNewSingleOrderInt(BaseMessageType):
    def __init__(self,
                 symbol=None,
                 exchange=None,
                 trade_account=None,
                 client_order_id=None,
                 order_type=None,
                 buy_sell=None,
                 price1=None,
                 price2=None,
                 divisor=None,
                 quantity=None,
                 time_in_force=None,
                 good_till_date_time=None,
                 is_automated_order=None,
                 is_parent_order=None,
                 free_form_text=None,
                 open_or_close=None):
        self.Type = MessageTypes.SUBMIT_NEW_SINGLE_ORDER_INT
        self.Symbol = symbol
        self.Exchange = exchange
        self.TradeAccount = trade_account
        self.ClientOrderID = client_order_id
        self.OrderType = order_type
        self.BuySell = buy_sell
        self.Price1 = price1
        self.Price2 = price2
        self.Divisor = divisor
        self.Quantity = quantity
        self.TimeInForce = time_in_force
        self.GoodTillDateTime = good_till_date_time
        self.IsAutomatedOrder = is_automated_order
        self.IsParentOrder = is_parent_order
        self.FreeFormText = free_form_text
        self.OpenOrClose = open_or_close

    @staticmethod
    def from_message_short(message_obj):
        packet = message_obj.get('F')
        return SubmitNewSingleOrderInt(
             symbol=packet[0],
             exchange=packet[1],
             trade_account=packet[2],
             client_order_id=packet[3],
             order_type=packet[4],
             buy_sell=packet[5],
             price1=packet[6],
             price2=packet[7],
             divisor=packet[8],
             quantity=packet[9],
             time_in_force=packet[10],
             good_till_date_time=packet[11],
             is_automated_order=packet[12],
             is_parent_order=packet[13],
             free_form_text=packet[14],
             open_or_close=packet[15]
        )

    @staticmethod
    def from_message_long(message_obj):
        return SubmitNewSingleOrderInt(
             symbol=message_obj.get('Symbol'),
             exchange=message_obj.get('Exchange'),
             trade_account=message_obj.get('TradeAccount'),
             client_order_id=message_obj.get('ClientOrderID'),
             order_type=message_obj.get('OrderType'),
             buy_sell=message_obj.get('BuySell'),
             price1=message_obj.get('Price1'),
             price2=message_obj.get('Price2'),
             divisor=message_obj.get('Divisor'),
             quantity=message_obj.get('Quantity'),
             time_in_force=message_obj.get('TimeInForce'),
             good_till_date_time=message_obj.get('GoodTillDateTime'),
             is_automated_order=message_obj.get('IsAutomatedOrder'),
             is_parent_order=message_obj.get('IsParentOrder'),
             free_form_text=message_obj.get('FreeFormText'),
             open_or_close=message_obj.get('OpenOrClose')
        )

    @staticmethod
    def from_message(message_obj):
        if 'F' in message_obj:
            return SubmitNewSingleOrderInt.from_message_short(message_obj)
        else:
            return SubmitNewSingleOrderInt.from_message_long(message_obj)

    @staticmethod
    def get_message_type_name():
        return "SubmitNewSingleOrderInt"
