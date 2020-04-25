
import json
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class MarketDataRequest(BaseMessageType):
    def __init__(self,
                 request_action=None,
                 symbol_id=None,
                 symbol=None,
                 exchange=None,
                 interval_for_snapshot_updates_in_milliseconds=None):
        self.Type = MessageTypes.MARKET_DATA_REQUEST
        self.RequestAction = request_action
        self.SymbolID = symbol_id
        self.Symbol = symbol
        self.Exchange = exchange
        self.IntervalForSnapshotUpdatesInMilliseconds = interval_for_snapshot_updates_in_milliseconds

