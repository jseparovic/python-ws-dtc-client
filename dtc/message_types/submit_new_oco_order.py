
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class SubmitNewOCOOrder(BaseMessageType):
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
                 open_or_close=None,
                 partial_fill_handling=None,
                 use_offsets=None,
                 offset_from_parent1=None,
                 offset_from_parent2=None):
        self.Type = MessageTypes.SUBMIT_NEW_OCO_ORDER
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
        self.OpenOrClose = open_or_close
        self.PartialFillHandling = partial_fill_handling
        self.UseOffsets = use_offsets
        self.OffsetFromParent1 = offset_from_parent1
        self.OffsetFromParent2 = offset_from_parent2

    @staticmethod
    def from_message_short(message_obj):
        packet = message_obj.get('F')
        return SubmitNewOCOOrder(
             symbol=packet[0],
             exchange=packet[1],
             client_order_id_1=packet[2],
             order_type_1=packet[3],
             buy_sell_1=packet[4],
             price1_1=packet[5],
             price2_1=packet[6],
             quantity_1=packet[7],
             client_order_id_2=packet[8],
             order_type_2=packet[9],
             buy_sell_2=packet[10],
             price1_2=packet[11],
             price2_2=packet[12],
             quantity_2=packet[13],
             time_in_force=packet[14],
             good_till_date_time=packet[15],
             trade_account=packet[16],
             is_automated_order=packet[17],
             parent_trigger_client_order_id=packet[18],
             free_form_text=packet[19],
             open_or_close=packet[20],
             partial_fill_handling=packet[21],
             use_offsets=packet[22],
             offset_from_parent1=packet[23],
             offset_from_parent2=packet[24]
        )

    @staticmethod
    def from_message_long(message_obj):
        return SubmitNewOCOOrder(
             symbol=message_obj.get('Symbol'),
             exchange=message_obj.get('Exchange'),
             client_order_id_1=message_obj.get('ClientOrderID_1'),
             order_type_1=message_obj.get('OrderType_1'),
             buy_sell_1=message_obj.get('BuySell_1'),
             price1_1=message_obj.get('Price1_1'),
             price2_1=message_obj.get('Price2_1'),
             quantity_1=message_obj.get('Quantity_1'),
             client_order_id_2=message_obj.get('ClientOrderID_2'),
             order_type_2=message_obj.get('OrderType_2'),
             buy_sell_2=message_obj.get('BuySell_2'),
             price1_2=message_obj.get('Price1_2'),
             price2_2=message_obj.get('Price2_2'),
             quantity_2=message_obj.get('Quantity_2'),
             time_in_force=message_obj.get('TimeInForce'),
             good_till_date_time=message_obj.get('GoodTillDateTime'),
             trade_account=message_obj.get('TradeAccount'),
             is_automated_order=message_obj.get('IsAutomatedOrder'),
             parent_trigger_client_order_id=message_obj.get('ParentTriggerClientOrderID'),
             free_form_text=message_obj.get('FreeFormText'),
             open_or_close=message_obj.get('OpenOrClose'),
             partial_fill_handling=message_obj.get('PartialFillHandling'),
             use_offsets=message_obj.get('UseOffsets'),
             offset_from_parent1=message_obj.get('OffsetFromParent1'),
             offset_from_parent2=message_obj.get('OffsetFromParent2')
        )

    @staticmethod
    def from_message(message_obj):
        if 'F' in message_obj:
            return SubmitNewOCOOrder.from_message_short(message_obj)
        else:
            return SubmitNewOCOOrder.from_message_long(message_obj)

    @staticmethod
    def get_message_type_name():
        return "SubmitNewOCOOrder"
