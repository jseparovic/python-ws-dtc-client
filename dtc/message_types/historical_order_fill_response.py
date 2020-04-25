
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

    @staticmethod
    def from_message_short(message_obj):
        packet = message_obj.get('F')
        return HistoricalOrderFillResponse(
             request_id=packet[0],
             total_number_messages=packet[1],
             message_number=packet[2],
             symbol=packet[3],
             exchange=packet[4],
             server_order_id=packet[5],
             buy_sell=packet[6],
             price=packet[7],
             date_time=packet[8],
             quantity=packet[9],
             unique_execution_id=packet[10],
             trade_account=packet[11],
             open_close=packet[12],
             no_order_fills=packet[13],
             info_text=packet[14],
             high_price_during_position=packet[15],
             low_price_during_position=packet[16],
             position_quantity=packet[17]
        )

    @staticmethod
    def from_message_long(message_obj):
        return HistoricalOrderFillResponse(
             request_id=message_obj.get('RequestID'),
             total_number_messages=message_obj.get('TotalNumberMessages'),
             message_number=message_obj.get('MessageNumber'),
             symbol=message_obj.get('Symbol'),
             exchange=message_obj.get('Exchange'),
             server_order_id=message_obj.get('ServerOrderID'),
             buy_sell=message_obj.get('BuySell'),
             price=message_obj.get('Price'),
             date_time=message_obj.get('DateTime'),
             quantity=message_obj.get('Quantity'),
             unique_execution_id=message_obj.get('UniqueExecutionID'),
             trade_account=message_obj.get('TradeAccount'),
             open_close=message_obj.get('OpenClose'),
             no_order_fills=message_obj.get('NoOrderFills'),
             info_text=message_obj.get('InfoText'),
             high_price_during_position=message_obj.get('HighPriceDuringPosition'),
             low_price_during_position=message_obj.get('LowPriceDuringPosition'),
             position_quantity=message_obj.get('PositionQuantity')
        )

    @staticmethod
    def from_message(message_obj):
        if 'F' in message_obj:
            return HistoricalOrderFillResponse.from_message_short(message_obj)
        else:
            return HistoricalOrderFillResponse.from_message_long(message_obj)

    @staticmethod
    def get_message_type_name():
        return "HistoricalOrderFillResponse"
