import collections
import json
import os
import signal
import sys
import time
from typing import List

import websocket  # pip install websocket_client
from geventwebsocket.exceptions import WebSocketError

from dtc.enums.logon_status_enum import LogonStatusEnum
from dtc.enums.request_action_enum import RequestActionEnum
from dtc.enums.trade_mode_enum import TradeModeEnum
from dtc.message_types.heartbeat import Heartbeat
from dtc.message_types.historical_price_data_request import HistoricalPriceDataRequest
from dtc.message_types.logon_request import LogonRequest
from dtc.message_types.logon_response import LogonResponse
from dtc.message_types.market_data_request import MarketDataRequest
from dtc.message_types.market_data_snapshot import MarketDataSnapshot
from dtc.util.message_util import MessageUtil
from dtc_client.data_message_types import MARKET_DATA_MESSAGE_TYPES, MARKET_DEPTH_MESSAGE_TYPES, HISTORICAL_DATA_MESSAGE_TYPES
from dtc_client.enums import SubscriptionDataType
from lib.base_message_type import BaseMessageType
from lib.error import LogonError, InvalidArgumentsError, RequestTimeoutError
from lib.symbol_util import get_symbol_id
from rest.rest_server import RESTServer

try:
    import thread
except ImportError:
    import _thread as thread

from lib.util import ArgParser, Util
import logging

DEFAULT_REST_PORT = 8080
DEFAULT_WS_PORT = 8090
CLIENT_NAME = 'DTC Client'
HEARTBEAT = 60
PROTOCOL_VERSION = 8

RESPONSE_TIMEOUT_MILLIS = 2000

PRETTY = True
DEFAULT_LOG_DATA = False
LOG_DATA = 'LOG_DATA'

REQUEST_ID = 'RequestID'
TOTAL_NUMBER_MESSAGES = 'TotalNumberMessages'
IS_FINAL_MESSAGE = 'IsFinalMessage'
SYMBOL = 'Symbol'


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


class Subscription:
    ws = None
    symbol = None
    data_type = None

    def __init__(self, ws, symbol, symbol_id, data_type):
        self.ws = ws
        self.symbol = symbol
        self.symbol_id = symbol_id
        self.data_type = data_type

    def equals(self, s):
        return self.ws == s.ws and self.symbol == s.symbol and self.data_type == s.data_type


class DTCClient:
    ws = None
    url = None
    is_logon = False
    responses = {}
    symbols = {}
    subscriptions: List[Subscription] = []

    def __init__(self, on_message_handler, post_login_thread=None):
        signal.signal(signal.SIGINT, self.exit)
        signal.signal(signal.SIGTERM, self.exit)
        self.stop = False
        self.on_message_handler = on_message_handler
        self.post_login_thread = post_login_thread
        self.parser = ArgParser(description=CLIENT_NAME)
        self.add_args()
        self.args = self.parser.parse_args()
        self.check_args()
        self.url = 'ws://%s:%s' % (self.args.host, self.args.port)
        logging.info('URL: %s' % self.url)
        self.trade_mode = TradeModeEnum.TRADE_MODE_LIVE if self.args.live else TradeModeEnum.TRADE_MODE_SIMULATED
        self.rest_server = RESTServer()
        self.rest_port = DEFAULT_REST_PORT if not self.args.restport else self.args.restport
        self.log_data = os.getenv(LOG_DATA) if os.getenv(LOG_DATA) and os.getenv(LOG_DATA) == 1 else DEFAULT_LOG_DATA

    def exit(self, signum, frame):
        self.stop = True
        sys.exit(0)

    def subscriptions_exist_for_symbol(self, symbol, data_type):
        for s in self.subscriptions:
            if s.symbol == symbol and s.data_type == data_type:
                return True
        return False

    def subscriptions_exist_for_socket(self, subscription):
        for s in self.subscriptions:
            if s.equals(subscription):
                return True
        return False

    def log_subscriptions(self):
        subs = []
        for s in self.subscriptions:
            subs.append({'symbol': s.symbol, 'dataType': s.data_type})
        logging.debug("Subscriptions: %s" % Util.json_dumps(subs))

    def data_subscribe(self, ws, symbol, data_type, record_interval=None, max_days_to_return=None):
        self.symbols[symbol] = get_symbol_id(symbol)
        subscription = Subscription(ws, symbol, self.symbols[symbol], data_type)

        # check for existing subscription
        if self.subscriptions_exist_for_socket(subscription):
            logging.debug("Subscription already exists.")
            self.log_subscriptions()
            return True

        if not self.subscriptions_exist_for_symbol(symbol, data_type):
            # only subscribe to the server once for all clients
            self.send_data_request(
                RequestActionEnum.SUBSCRIBE, data_type, symbol, record_interval, max_days_to_return)

        self.subscriptions.append(subscription)
        self.log_subscriptions()
        return True

    def remove_subscription(self, subscription):
        ix_to_delete = []
        for i, s in enumerate(self.subscriptions):
            if s.equals(subscription):
                ix_to_delete.insert(0, i)
        for i in ix_to_delete:
            del self.subscriptions[i]

    def data_unsubscribe_all_for_socket(self, ws):
        for s in self.subscriptions:
            if s.ws == ws:
                self.data_unsubscribe(ws, s.symbol, s.data_type)

    def send_data_request(self, request_action, data_type, symbol, record_interval=None, max_days_to_return=None):
        if data_type == SubscriptionDataType.MARKET:
            self.send(
                MarketDataRequest(
                    request_action=request_action,
                    symbol_id=self.symbols[symbol],
                    symbol=symbol))
        elif data_type == SubscriptionDataType.HISTORICAL:
            self.send(
                HistoricalPriceDataRequest(
                    request_action=request_action,
                    symbol_id=self.symbols[symbol],
                    symbol=symbol,
                    record_interval=record_interval,
                    max_days_to_return=max_days_to_return,
                ))

    def data_unsubscribe(self, ws, symbol, data_type, record_interval=None, max_days_to_return=None):
        subscription = Subscription(ws, symbol, self.symbols[symbol], data_type)
        if not self.subscriptions_exist_for_socket(subscription):
            logging.debug("Subscription does not exist.")
            self.log_subscriptions()
            return True

        self.remove_subscription(subscription)

        if not self.subscriptions_exist_for_symbol(symbol, data_type):
            # only unsubscribe to the server once for all clients
            self.send_data_request(
                RequestActionEnum.UNSUBSCRIBE, data_type, symbol, record_interval, max_days_to_return)

        self.log_subscriptions()
        return True

    def send(self, message: BaseMessageType):
        logging.debug('Sending %s:\n%s' % (message.get_message_type_name(), message.to_JSON(pretty=PRETTY)))
        self.ws.send(message.to_JSON(logging=False) + '\x00')  # must be null terminated

    def request_response(self, request_id, request):
        if self.is_logon:
            self.send(request)
            self.responses[request_id] = Response(request_id)
            start_time = time.time()
            while not self.responses[request_id].is_complete():
                time.sleep(0.0001)
                if time.time() > start_time + RESPONSE_TIMEOUT_MILLIS/1000:
                    logging.warning('Request %s has timed out' % request_id)
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

    @staticmethod
    def is_data(message):
        return message.Type in MARKET_DATA_MESSAGE_TYPES + MARKET_DEPTH_MESSAGE_TYPES + HISTORICAL_DATA_MESSAGE_TYPES

    @staticmethod
    def is_market_data(message):
        return message.Type in MARKET_DATA_MESSAGE_TYPES

    @staticmethod
    def is_market_depth(message):
        return message.Type in MARKET_DEPTH_MESSAGE_TYPES

    @staticmethod
    def is_historical_data(message):
        return message.Type in HISTORICAL_DATA_MESSAGE_TYPES

    def on_message(self, message_text):
        message = MessageUtil.parse_incoming_message(message_text)

        if self.log_data or not self.is_data(message):
            logging.debug('Received %s:\n%s' % (message.get_message_type_name(), message.to_JSON(pretty=PRETTY)))

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
                if self.is_market_data(message):
                    # Send to Market Data Subscriptions
                    for s in self.subscriptions:
                        if s.symbol_id == message.SymbolID and s.data_type == SubscriptionDataType.MARKET:
                            # Add the symbol to the response and sort keys
                            result = json.loads(message.to_JSON())
                            result[SYMBOL] = s.symbol
                            result = collections.OrderedDict(sorted(result.items()))
                            try:
                                s.ws.send(json.dumps(result))
                            except WebSocketError as e:
                                logging.warning(e)
                                self.data_unsubscribe_all_for_socket(s.ws)

                # send to the callback
                if self.on_message_handler:
                    thread.start_new_thread(self.on_message_handler, (message,))

    def on_error(self, error):
        logging.error('Error: %s' % error)

    def on_close(self):
        logging.info('Closing')

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
            try:
                self.ws.run_forever()
            except BaseException as e:
                if self.stop:
                    break
                else:
                    raise e

            logging.error('Server stopped. Restarting...')
            time.sleep(5)

    def check_args(self):
        if self.args.live and self.args.simulated:
            raise InvalidArgumentsError('Select live or simulated mode but not both')
        if not self.args.live and not self.args.simulated:
            raise InvalidArgumentsError('Select live or simulated mode')

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
                                 help='Local REST Server Port',
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

