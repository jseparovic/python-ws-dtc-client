
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class Heartbeat(BaseMessageType):
    def __init__(self,
                 num_dropped_messages=None,
                 current_date_time=None):
        self.Type = MessageTypes.HEARTBEAT
        self.NumDroppedMessages = num_dropped_messages
        self.CurrentDateTime = current_date_time

    @staticmethod
    def from_message_short(message_obj):
        packet = message_obj.get('F')
        return Heartbeat(
             num_dropped_messages=packet[0],
             current_date_time=packet[1]
        )

    @staticmethod
    def from_message_long(message_obj):
        return Heartbeat(
             num_dropped_messages=message_obj.get('NumDroppedMessages'),
             current_date_time=message_obj.get('CurrentDateTime')
        )

    @staticmethod
    def from_message(message_obj):
        if 'F' in message_obj:
            return Heartbeat.from_message_short(message_obj)
        else:
            return Heartbeat.from_message_long(message_obj)

    @staticmethod
    def get_message_type_name():
        return "Heartbeat"
