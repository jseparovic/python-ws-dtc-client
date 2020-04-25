
import json
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class JournalEntriesRequest(BaseMessageType):
    def __init__(self,
                 request_id=None,
                 start_date_time=None):
        self.Type = MessageTypes.JOURNAL_ENTRIES_REQUEST
        self.RequestID = request_id
        self.StartDateTime = start_date_time

