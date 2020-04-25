
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class JournalEntryAdd(BaseMessageType):
    def __init__(self,
                 journal_entry=None,
                 date_time=None):
        self.Type = MessageTypes.JOURNAL_ENTRY_ADD
        self.JournalEntry = journal_entry
        self.DateTime = date_time

    @staticmethod
    def from_message(message_obj):
        return JournalEntryAdd(
             journal_entry=message_obj.get('JournalEntry'),
             date_time=message_obj.get('DateTime')
        )

    @staticmethod
    def get_message_type_name():
        return "JournalEntryAdd"
