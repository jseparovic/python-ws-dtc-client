import time
import websocket  # pip install websocket_client

from dtc.enums.logon_status_enum import LogonStatusEnum
from dtc.enums.trade_mode_enum import TradeModeEnum
from dtc.message_types.heartbeat import Heartbeat
from dtc.message_types.logon_request import LogonRequest
from dtc.message_types.logon_response import LogonResponse
from dtc.util.message_util import MessageUtil
from lib.base_message_type import BaseMessageType
from lib.error import LogonError, InvalidArgumentsError

try:
    import thread
except ImportError:
    import _thread as thread

from lib.util import ArgParser
import logging

CLIENT_NAME = "DTC Client"
HEARTBEAT = 60
PROTOCOL_VERSION = 8

PRETTY = True


class DTCClient:
    ws = None
    url = None
    request_id = 0
    is_logon = False

    def __init__(self, on_message_handler, post_login_thread=None):
        self.on_message_handler = on_message_handler
        self.post_login_thread = post_login_thread
        self.parser = ArgParser(description=CLIENT_NAME)
        self.add_args()
        self.args = self.parser.parse_args()
        self.check_args()
        self.url = 'ws://%s:%s' % (self.args.host, self.args.port)
        logging.info("URL: %s" % self.url)
        self.trade_mode = TradeModeEnum.TRADE_MODE_LIVE if self.args.live else TradeModeEnum.TRADE_MODE_SIMULATED

    def send(self, message: BaseMessageType):
        logging.debug("Sending %s:\n%s" % (message.get_message_type_name(), message.to_JSON(pretty=PRETTY)))
        self.ws.send(message.to_JSON(logging=False) + '\x00')  # must be null terminated

    def on_message(self, message_text):
        message = MessageUtil.parse_incoming_message(message_text)
        logging.debug("Received %s:\n%s" % (message.get_message_type_name(), message.to_JSON(pretty=PRETTY)))

        if isinstance(message, LogonResponse):
            logonResponse: LogonResponse = message
            if logonResponse.Result != LogonStatusEnum.LOGON_SUCCESS:
                raise LogonError
            self.is_logon = True

            if self.post_login_thread:
                thread.start_new_thread(self.post_login_thread, ())

        elif isinstance(message, Heartbeat):
            # send heartbeat back
            self.send(
                Heartbeat(
                    current_date_time=time.time(),
                ))

        else:
            thread.start_new_thread(self.on_message_handler, (message,))

    def on_error(self, error):
        logging.error("Error: %s" % error)

    def on_close(self):
        logging.info("Closing")

    def on_open(self):
        self.send(
            LogonRequest(
                username=self.args.username,
                password=self.args.password,
                trade_mode=self.trade_mode,
                protocol_version=PROTOCOL_VERSION,
                heartbeat_interval_in_seconds=HEARTBEAT,
                client_name=CLIENT_NAME
            ))

    def start(self):
        def on_message(ws, message):
            self.on_message(message)

        def on_error(ws, error):
            self.on_error(error)

        def on_close(ws):
            self.on_close()

        def on_open(ws):
            self.on_open()

        # websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp(self.url,
                                         on_message=on_message,
                                         on_error=on_error,
                                         on_close=on_close)
        self.ws.on_open = on_open
        self.ws.run_forever()

    def check_args(self):
        if self.args.live and self.args.simulated:
            raise InvalidArgumentsError("Select live or simulated mode but not both")
        if not self.args.live and not self.args.simulated:
            raise InvalidArgumentsError("Select live or simulated mode")

    def add_args(self):
        self.parser.add_argument('-n', '--host',
                                 help='Websocket Host',
                                 action='store',
                                 required=True)
        self.parser.add_argument('-p', '--port',
                                 help='Websocket Port',
                                 action='store',
                                 required=True)
        self.parser.add_argument('-l', '--live',
                                 help='Live trading mode',
                                 action='store_true')
        self.parser.add_argument('-s', '--simulated',
                                 help='Simulated trading mode',
                                 action='store_true')
        self.parser.add_argument('-u', '--username',
                                 help='Server Username',
                                 action='store')
        self.parser.add_argument('-x', '--password',
                                 help='Server Password',
                                 action='store')
