
import json
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

