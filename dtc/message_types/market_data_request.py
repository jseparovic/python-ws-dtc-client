
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

    @staticmethod
    def from_message_short(message_obj):
        packet = message_obj.get('F')
        return MarketDataRequest(
             request_action=packet[0],
             symbol_id=packet[1],
             symbol=packet[2],
             exchange=packet[3],
             interval_for_snapshot_updates_in_milliseconds=packet[4]
        )

    @staticmethod
    def from_message_long(message_obj):
        return MarketDataRequest(
             request_action=message_obj.get('RequestAction'),
             symbol_id=message_obj.get('SymbolID'),
             symbol=message_obj.get('Symbol'),
             exchange=message_obj.get('Exchange'),
             interval_for_snapshot_updates_in_milliseconds=message_obj.get('IntervalForSnapshotUpdatesInMilliseconds')
        )

    @staticmethod
    def from_message(message_obj):
        if 'F' in message_obj:
            return MarketDataRequest.from_message_short(message_obj)
        else:
            return MarketDataRequest.from_message_long(message_obj)

    @staticmethod
    def get_message_type_name():
        return "MarketDataRequest"
