
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

    @staticmethod
    def from_message(message_obj):
        return LogonRequest(
             protocol_version=message_obj.get('ProtocolVersion'),
             username=message_obj.get('Username'),
             password=message_obj.get('Password'),
             general_text_data=message_obj.get('GeneralTextData'),
             integer_1=message_obj.get('Integer_1'),
             integer_2=message_obj.get('Integer_2'),
             heartbeat_interval_in_seconds=message_obj.get('HeartbeatIntervalInSeconds'),
             trade_mode=message_obj.get('TradeMode'),
             trade_account=message_obj.get('TradeAccount'),
             hardware_identifier=message_obj.get('HardwareIdentifier'),
             client_name=message_obj.get('ClientName')
        )

    @staticmethod
    def get_message_type_name():
        return "LogonRequest"
