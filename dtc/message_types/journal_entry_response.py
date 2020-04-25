
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class JournalEntryResponse(BaseMessageType):
    def __init__(self,
                 journal_entry=None,
                 date_time=None,
                 is_final_response=None):
        self.Type = MessageTypes.JOURNAL_ENTRY_RESPONSE
        self.JournalEntry = journal_entry
        self.DateTime = date_time
        self.IsFinalResponse = is_final_response

    @staticmethod
    def from_message(message_obj):
        return JournalEntryResponse(
             journal_entry=message_obj.get('JournalEntry'),
             date_time=message_obj.get('DateTime'),
             is_final_response=message_obj.get('IsFinalResponse')
        )

    @staticmethod
    def get_message_type_name():
        return "JournalEntryResponse"
