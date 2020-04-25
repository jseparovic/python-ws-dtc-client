
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class PositionUpdate(BaseMessageType):
    def __init__(self,
                 request_id=None,
                 total_number_messages=None,
                 message_number=None,
                 symbol=None,
                 exchange=None,
                 quantity=None,
                 average_price=None,
                 position_identifier=None,
                 trade_account=None,
                 no_positions=None,
                 unsolicited=None,
                 margin_requirement=None,
                 entry_date_time=None):
        self.Type = MessageTypes.POSITION_UPDATE
        self.RequestID = request_id
        self.TotalNumberMessages = total_number_messages
        self.MessageNumber = message_number
        self.Symbol = symbol
        self.Exchange = exchange
        self.Quantity = quantity
        self.AveragePrice = average_price
        self.PositionIdentifier = position_identifier
        self.TradeAccount = trade_account
        self.NoPositions = no_positions
        self.Unsolicited = unsolicited
        self.MarginRequirement = margin_requirement
        self.EntryDateTime = entry_date_time

    @staticmethod
    def from_message_short(message_obj):
        packet = message_obj.get('F')
        return PositionUpdate(
             request_id=packet[0],
             total_number_messages=packet[1],
             message_number=packet[2],
             symbol=packet[3],
             exchange=packet[4],
             quantity=packet[5],
             average_price=packet[6],
             position_identifier=packet[7],
             trade_account=packet[8],
             no_positions=packet[9],
             unsolicited=packet[10],
             margin_requirement=packet[11],
             entry_date_time=packet[12]
        )

    @staticmethod
    def from_message_long(message_obj):
        return PositionUpdate(
             request_id=message_obj.get('RequestID'),
             total_number_messages=message_obj.get('TotalNumberMessages'),
             message_number=message_obj.get('MessageNumber'),
             symbol=message_obj.get('Symbol'),
             exchange=message_obj.get('Exchange'),
             quantity=message_obj.get('Quantity'),
             average_price=message_obj.get('AveragePrice'),
             position_identifier=message_obj.get('PositionIdentifier'),
             trade_account=message_obj.get('TradeAccount'),
             no_positions=message_obj.get('NoPositions'),
             unsolicited=message_obj.get('Unsolicited'),
             margin_requirement=message_obj.get('MarginRequirement'),
             entry_date_time=message_obj.get('EntryDateTime')
        )

    @staticmethod
    def from_message(message_obj):
        if 'F' in message_obj:
            return PositionUpdate.from_message_short(message_obj)
        else:
            return PositionUpdate.from_message_long(message_obj)

    @staticmethod
    def get_message_type_name():
        return "PositionUpdate"
