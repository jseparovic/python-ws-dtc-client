
import json
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class HistoricalOrderFillResponse(BaseMessageType):
    def __init__(self,
                 request_id=None,
                 total_number_messages=None,
                 message_number=None,
                 symbol=None,
                 exchange=None,
                 server_order_id=None,
                 buy_sell=None,
                 price=None,
                 date_time=None,
                 quantity=None,
                 unique_execution_id=None,
                 trade_account=None,
                 open_close=None,
                 no_order_fills=None,
                 info_text=None,
                 high_price_during_position=None,
                 low_price_during_position=None,
                 position_quantity=None):
        self.Type = MessageTypes.HISTORICAL_ORDER_FILL_RESPONSE
        self.RequestID = request_id
        self.TotalNumberMessages = total_number_messages
        self.MessageNumber = message_number
        self.Symbol = symbol
        self.Exchange = exchange
        self.ServerOrderID = server_order_id
        self.BuySell = buy_sell
        self.Price = price
        self.DateTime = date_time
        self.Quantity = quantity
        self.UniqueExecutionID = unique_execution_id
        self.TradeAccount = trade_account
        self.OpenClose = open_close
        self.NoOrderFills = no_order_fills
        self.InfoText = info_text
        self.HighPriceDuringPosition = high_price_during_position
        self.LowPriceDuringPosition = low_price_during_position
        self.PositionQuantity = position_quantity

