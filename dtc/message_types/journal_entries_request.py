
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class JournalEntriesRequest(BaseMessageType):
    def __init__(self,
                 request_id=None,
                 start_date_time=None):
        self.Type = MessageTypes.JOURNAL_ENTRIES_REQUEST
        self.RequestID = request_id
        self.StartDateTime = start_date_time

    @staticmethod
    def from_message_short(message_obj):
        packet = message_obj.get('F')
        return JournalEntriesRequest(
             request_id=packet[0],
             start_date_time=packet[1]
        )

    @staticmethod
    def from_message_long(message_obj):
        return JournalEntriesRequest(
             request_id=message_obj.get('RequestID'),
             start_date_time=message_obj.get('StartDateTime')
        )

    @staticmethod
    def from_message(message_obj):
        if 'F' in message_obj:
            return JournalEntriesRequest.from_message_short(message_obj)
        else:
            return JournalEntriesRequest.from_message_long(message_obj)

    @staticmethod
    def get_message_type_name():
        return "JournalEntriesRequest"
