
import json
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class LogonRequest(BaseMessageType):
    def __init__(self,
                 protocol_version=None,
                 username=None,
                 password=None,
                 general_text_data=None,
                 integer_1=None,
                 integer_2=None,
                 heartbeat_interval_in_seconds=None,
                 trade_mode=None,
                 trade_account=None,
                 hardware_identifier=None,
                 client_name=None):
        self.Type = MessageTypes.LOGON_REQUEST
        self.ProtocolVersion = protocol_version
        self.Username = username
        self.Password = password
        self.GeneralTextData = general_text_data
        self.Integer_1 = integer_1
        self.Integer_2 = integer_2
        self.HeartbeatIntervalInSeconds = heartbeat_interval_in_seconds
        self.TradeMode = trade_mode
        self.TradeAccount = trade_account
        self.HardwareIdentifier = hardware_identifier
        self.ClientName = client_name

