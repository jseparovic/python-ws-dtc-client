
import json
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class OrderUpdate(BaseMessageType):
    def __init__(self,
                 request_id=None,
                 total_num_messages=None,
                 message_number=None,
                 symbol=None,
                 exchange=None,
                 previous_server_order_id=None,
                 server_order_id=None,
                 client_order_id=None,
                 exchange_order_id=None,
                 order_status=None,
                 order_update_reason=None,
                 order_type=None,
                 buy_sell=None,
                 price1=None,
                 price2=None,
                 time_in_force=None,
                 good_till_date_time=None,
                 order_quantity=None,
                 filled_quantity=None,
                 remaining_quantity=None,
                 average_fill_price=None,
                 last_fill_price=None,
                 last_fill_date_time=None,
                 last_fill_quantity=None,
                 last_fill_execution_id=None,
                 trade_account=None,
                 info_text=None,
                 no_orders=None,
                 parent_server_order_id=None,
                 o_c_o_linked_order_server_order_id=None,
                 open_or_close=None,
                 previous_client_order_id=None,
                 free_form_text=None,
                 order_received_date_time=None,
                 latest_transaction_date_time=None):
        self.Type = MessageTypes.ORDER_UPDATE
        self.RequestID = request_id
        self.TotalNumMessages = total_num_messages
        self.MessageNumber = message_number
        self.Symbol = symbol
        self.Exchange = exchange
        self.PreviousServerOrderID = previous_server_order_id
        self.ServerOrderID = server_order_id
        self.ClientOrderID = client_order_id
        self.ExchangeOrderID = exchange_order_id
        self.OrderStatus = order_status
        self.OrderUpdateReason = order_update_reason
        self.OrderType = order_type
        self.BuySell = buy_sell
        self.Price1 = price1
        self.Price2 = price2
        self.TimeInForce = time_in_force
        self.GoodTillDateTime = good_till_date_time
        self.OrderQuantity = order_quantity
        self.FilledQuantity = filled_quantity
        self.RemainingQuantity = remaining_quantity
        self.AverageFillPrice = average_fill_price
        self.LastFillPrice = last_fill_price
        self.LastFillDateTime = last_fill_date_time
        self.LastFillQuantity = last_fill_quantity
        self.LastFillExecutionID = last_fill_execution_id
        self.TradeAccount = trade_account
        self.InfoText = info_text
        self.NoOrders = no_orders
        self.ParentServerOrderID = parent_server_order_id
        self.OCOLinkedOrderServerOrderID = o_c_o_linked_order_server_order_id
        self.OpenOrClose = open_or_close
        self.PreviousClientOrderID = previous_client_order_id
        self.FreeFormText = free_form_text
        self.OrderReceivedDateTime = order_received_date_time
        self.LatestTransactionDateTime = latest_transaction_date_time

