import time

# pip install websocket_client
import websocket

from dtc.enums.trade_mode_enum import TradeModeEnum
from dtc.message_types.logon_request import LogonRequest
from lib.base_message_type import BaseMessageType

try:
    import thread
except ImportError:
    import _thread as thread

from lib.util import Util, ArgParser, CONSOLE_LOGGING
import logging

CLIENT_NAME = "DTC Client"
HEARTBEAT = 120
PROTOCOL_VERSION = 8


class DTCClient:
    ws = None
    url = None

    def __init__(self):
        self.parser = ArgParser(description='DTC Client')
        self.add_args()
        self.args = self.parser.parse_args()
        self.check_args()
        self.url = 'ws://%s:%s' % (self.args.host, self.args.port)
        logging.info("URL: %s" % self.url)

    def receive(self):
        result = self.ws.recv()
        logging.info('Result: {}'.format(result))

    def send(self, message: BaseMessageType):
        self.ws.send(message.to_JSON() + '\x00')  # must be null terminated

    def on_message(self, message):
        logging.info("on_message: %s" % message)
        # handle logon response here
        # then do more stuff

    def on_error(self, error):
        logging.error("on_error: %s" % error)

    def on_close(self):
        logging.info("on_close")

    def on_open(self):
        self.send(
            LogonRequest(
                username=self.args.username,
                password=self.args.password,
                trade_mode=TradeModeEnum.TRADE_MODE_LIVE,
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
        # check args here if needed:
        pass

    def add_args(self):
        self.parser.add_argument('-n', '--host',
                                 help='Websocket Host',
                                 action='store',
                                 required=True)
        self.parser.add_argument('-p', '--port',
                                 help='Websocket Port',
                                 action='store',
                                 required=True)
        self.parser.add_argument('-u', '--username',
                                 help='Server Username',
                                 action='store')
        self.parser.add_argument('-x', '--password',
                                 help='Server Password',
                                 action='store')


if __name__ == '__main__':
    logger = Util.setup_logging("DTC_Client", console=CONSOLE_LOGGING)
    dtc_client = DTCClient()
    dtc_client.start()

