import json
import time
import websocket  # pip install websocket_client

from rest.rest_server import RESTServer
from dtc.enums.logon_status_enum import LogonStatusEnum
from dtc.enums.trade_mode_enum import TradeModeEnum
from dtc.message_types.heartbeat import Heartbeat
from dtc.message_types.logon_request import LogonRequest
from dtc.message_types.logon_response import LogonResponse
from dtc.util.message_util import MessageUtil
from lib.base_message_type import BaseMessageType
from lib.error import LogonError, InvalidArgumentsError, RequestTimeoutError

try:
    import thread
except ImportError:
    import _thread as thread

from lib.util import ArgParser
import logging

DEFAULT_REST_PORT = 8080
CLIENT_NAME = "DTC Client"
HEARTBEAT = 60
PROTOCOL_VERSION = 8

RESPONSE_TIMEOUT_MILLIS = 2000

PRETTY = True

REQUEST_ID = "RequestID"
TOTAL_NUMBER_MESSAGES = "TotalNumberMessages"
IS_FINAL_MESSAGE = "IsFinalMessage"

class Response:
    def __init__(self, request_id):
        self.request_id = request_id
        self.messages = []
        self.total_number_messages = None
        self.is_final_message = False

    def new_message(self, message, total_number_messages=None, is_final_message=None):
        self.messages.append(message)
        if not self.total_number_messages and total_number_messages:
            self.total_number_messages = total_number_messages
        if is_final_message:
            self.is_final_message = True

    def is_complete(self):
        return self.is_final_message \
               or (self.total_number_messages and self.total_number_messages == len(self.messages))


class DTCClient:
    ws = None
    url = None
    is_logon = False
    responses = {}

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
        self.rest_server = RESTServer()
        self.rest_port = DEFAULT_REST_PORT if not self.args.restport else self.args.restport

    def send(self, message: BaseMessageType):
        logging.debug("Sending %s:\n%s" % (message.get_message_type_name(), message.to_JSON(pretty=PRETTY)))
        self.ws.send(message.to_JSON(logging=False) + '\x00')  # must be null terminated

    def request_response(self, request_id, request):
        if self.is_logon:
            self.send(request)
            self.responses[request_id] = Response(request_id)
            start_time = time.time()
            while not self.responses[request_id].is_complete():
                time.sleep(0.0001)
                if time.time() > start_time + RESPONSE_TIMEOUT_MILLIS/1000:
                    logging.warning("Request %s has timed out" % request_id)
                    del self.responses[request_id]
                    raise RequestTimeoutError
            response = self.responses[request_id].messages
            del self.responses[request_id]
            json_response = []
            for r in response:
                json_response.append(json.loads(r.to_JSON()))
            return json_response
        else:
            raise LogonError

    def on_message(self, message_text):
        message = MessageUtil.parse_incoming_message(message_text)
        logging.debug("Received %s:\n%s" % (message.get_message_type_name(), message.to_JSON(pretty=PRETTY)))

        message_obj = json.loads(message.to_JSON())

        if REQUEST_ID in message_obj and message_obj[REQUEST_ID] in self.responses:
            # Handle waiting requests
            if TOTAL_NUMBER_MESSAGES in message_obj:
                total_number_messages = message_obj[TOTAL_NUMBER_MESSAGES]
                self.responses[message_obj[REQUEST_ID]].new_message(
                    message, total_number_messages=total_number_messages)
            elif IS_FINAL_MESSAGE not in message_obj:
                self.responses[message_obj[REQUEST_ID]].new_message(
                    message, total_number_messages=1)
            else:
                self.responses[message_obj[REQUEST_ID]].new_message(
                    message, is_final_message=bool(message_obj[IS_FINAL_MESSAGE]))

        else:
            if isinstance(message, LogonResponse):
                # Handle Login response
                logonResponse: LogonResponse = message
                if logonResponse.Result != LogonStatusEnum.LOGON_SUCCESS:
                    raise LogonError
                self.is_logon = True

                if self.post_login_thread:
                    thread.start_new_thread(self.post_login_thread, ())

                # start rest server
                thread.start_new_thread(self.rest_server.start, (self, self.rest_port))

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

        while True:
            # websocket.enableTrace(True)
            self.ws = websocket.WebSocketApp(self.url,
                                             on_message=on_message,
                                             on_error=on_error,
                                             on_close=on_close)
            self.ws.on_open = on_open
            self.ws.run_forever()
            logging.error("Server stopped. Restarting...")
            time.sleep(5)

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
        self.parser.add_argument('-r', '--restport',
                                 help='REST Server Port',
                                 action='store',
                                 type=int)
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

