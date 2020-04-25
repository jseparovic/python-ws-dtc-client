
import json
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class HistoricalPriceDataRecordResponse::union (BaseMessageType):
    def __init__(self,
                 open_interest=None,
                 num_trades=None):
        self.Type = MessageTypes.HISTORICAL_PRICE_DATA_RECORD_RESPONSE::UNION 
        self.OpenInterest = open_interest
        self.NumTrades = num_trades

