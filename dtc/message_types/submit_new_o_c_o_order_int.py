
import json
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class SubmitNewOCOOrderInt(BaseMessageType):
    def __init__(self,
                 symbol=None,
                 exchange=None,
                 client_order_id_1=None,
                 order_type_1=None,
                 buy_sell_1=None,
                 price1_1=None,
                 price2_1=None,
                 quantity_1=None,
                 client_order_id_2=None,
                 order_type_2=None,
                 buy_sell_2=None,
                 price1_2=None,
                 price2_2=None,
                 quantity_2=None,
                 time_in_force=None,
                 good_till_date_time=None,
                 trade_account=None,
                 is_automated_order=None,
                 parent_trigger_client_order_id=None,
                 free_form_text=None,
                 divisor=None,
                 open_or_close=None,
                 partial_fill_handling=None):
        self.Type = MessageTypes.SUBMIT_NEW_O_C_O_ORDER_INT
        self.Symbol = symbol
        self.Exchange = exchange
        self.ClientOrderID_1 = client_order_id_1
        self.OrderType_1 = order_type_1
        self.BuySell_1 = buy_sell_1
        self.Price1_1 = price1_1
        self.Price2_1 = price2_1
        self.Quantity_1 = quantity_1
        self.ClientOrderID_2 = client_order_id_2
        self.OrderType_2 = order_type_2
        self.BuySell_2 = buy_sell_2
        self.Price1_2 = price1_2
        self.Price2_2 = price2_2
        self.Quantity_2 = quantity_2
        self.TimeInForce = time_in_force
        self.GoodTillDateTime = good_till_date_time
        self.TradeAccount = trade_account
        self.IsAutomatedOrder = is_automated_order
        self.ParentTriggerClientOrderID = parent_trigger_client_order_id
        self.FreeFormText = free_form_text
        self.Divisor = divisor
        self.OpenOrClose = open_or_close
        self.PartialFillHandling = partial_fill_handling

