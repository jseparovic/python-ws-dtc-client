import json
import logging
from threading import Lock

from flask import Flask, request, jsonify
from flask_sockets import Sockets

from dtc.message_types.account_balance_request import AccountBalanceRequest
from dtc.message_types.current_positions_request import CurrentPositionsRequest
from dtc.message_types.exchange_list_request import ExchangeListRequest
from dtc.message_types.historical_account_balances_request import HistoricalAccountBalancesRequest
from dtc.message_types.historical_order_fills_request import HistoricalOrderFillsRequest
from dtc.message_types.security_definition_for_symbol_request import SecurityDefinitionForSymbolRequest
from dtc.message_types.trade_accounts_request import TradeAccountsRequest
from lib.error import MethodNotAllowedError, InvalidArgumentsError, RequestTimeoutError
from rest.api import API

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['DEBUG'] = True
sockets = Sockets(app)

PRETTY = True

dtc_client = None
rest_server = None

TRADE_ACCOUNT = 'TradeAccount'
NUMBER_OF_DAYS = 'NumberOfDays'
START_DATE_TIME = 'StartDateTime'
SYMBOL = 'Symbol'
EXCHANGE = 'Exchange'


# Subscription keys
_ACTION = 'action'
_SUBSCRIBE = 'subscribe'
_UNSUBSCRIBE = 'unsubscribe'
_SYMBOL = 'symbol'
_SUCCESS = 'success'


@sockets.route(API.API_PREFIX + API.MARKET_DATA)
def market_data(ws):
    logging.info('ws connected')
    while not ws.closed:
        try:
            request = json.loads(ws.receive())
            action = request.get(_ACTION)

            if action in [_SUBSCRIBE, _UNSUBSCRIBE]:
                symbol = request.get(_SYMBOL)
                success = False
                if action == _SUBSCRIBE:
                    if dtc_client.market_data_subscribe(ws, symbol):
                        success = True
                else:  # action == _UNSUBSCRIBE
                    if dtc_client.market_data_unsubscribe(ws, symbol):
                        success = True

                message = {_ACTION: action, _SYMBOL: symbol, _SUCCESS: success}
                ws.send(json.dumps(message))
            else:
                ws.send(json.dumps(
                    {'error': 'unknown_action', 'details': 'action=subscribe|unsubscribe, symbol=symbol'}))
        except Exception as e:
            logging.debug(e)
            ws.closed

    dtc_client.market_data_unsubscribe_all_for_socket(ws)


def handle_request(json):
    print('received json: ' + str(json))


@app.errorhandler(InvalidArgumentsError)
def handle_invalid_arguments_error(error):
    logging.error(error)
    status_code = 400
    success = False
    response = {
        'success': success,
        'error': {
            'type': 'InvalidArgumentsError',
            'message': error.__str__(),
            'status': status_code
        }
    }
    return jsonify(response), status_code


@app.errorhandler(MethodNotAllowedError)
def handle_method_not_allowed_error(error):
    logging.error(error)
    status_code = 405
    success = False
    response = {
        'success': success,
        'error': {
            'type': 'MethodNotAllowedError',
            'message': 'The request method is not allowed.',
            'status': status_code
       }
    }
    return jsonify(response), status_code


@app.errorhandler(404)
def handle_not_found(error):
    logging.error(error)
    status_code = 404
    success = False
    response = {
        'success': success,
        'error': {
            'type': 'NotFoundError',
            'message': error.__str__(),
            'status': status_code
        }
    }
    return jsonify(response), status_code


@app.errorhandler(RequestTimeoutError)
def handle_request_timeout(error):
    logging.error(error)
    status_code = 408
    success = False
    response = {
        'success': success,
        'error': {
            'type': 'RequestTimeoutError',
            'message': 'The request timed out.',
            'status': status_code
       }
    }
    return jsonify(response), status_code


@app.errorhandler(Exception)
def handle_unexpected_error(error):
    logging.error(error)
    status_code = 500
    success = False
    response = {
        'success': success,
        'error': {
            'type': 'UnexpectedError',
            'message': 'An unexpected error has occurred.',
            'status': status_code
        }
    }
    return jsonify(response), status_code


@app.route(API.API_PREFIX + API.ACCOUNT_BALANCE)
def account_balance():
    request_id = rest_server.get_next_request_id()
    response = dtc_client.request_response(
        request_id,
        AccountBalanceRequest(
            request_id=request_id
        )
    )
    return jsonify(response)


@app.route(API.API_PREFIX + API.CURRENT_POSITIONS)
def current_positions():
    request_id = rest_server.get_next_request_id()
    response = dtc_client.request_response(
        request_id,
        CurrentPositionsRequest(
            request_id=request_id
        )
    )
    return jsonify(response)


@app.route(API.API_PREFIX + API.EXCHANGE_LIST)
def exchange_list():
    request_id = rest_server.get_next_request_id()
    response = dtc_client.request_response(
        request_id,
        ExchangeListRequest(
            request_id=request_id
        )
    )
    return jsonify(response)


@app.route(API.API_PREFIX + API.HISTORICAL_ACCOUNT_BALANCES)
def historical_account_balance():
    trade_account = rest_server.get_query_param(TRADE_ACCOUNT)
    start_date_time = rest_server.get_query_param(START_DATE_TIME, required=False)
    request_id = rest_server.get_next_request_id()

    response = dtc_client.request_response(
        request_id,
        HistoricalAccountBalancesRequest(
            request_id=request_id,
            trade_account=trade_account,
            start_date_time=start_date_time
        )
    )
    return jsonify(response)


@app.route(API.API_PREFIX + API.HISTORICAL_ORDER_FILLS)
def historical_order_fills():
    trade_account = rest_server.get_query_param(TRADE_ACCOUNT)
    number_of_days = rest_server.get_query_param(NUMBER_OF_DAYS, required=False)
    start_date_time = rest_server.get_query_param(START_DATE_TIME, required=False)
    if not number_of_days and not start_date_time:
        raise InvalidArgumentsError('Either %s or %s must be specified' % (NUMBER_OF_DAYS, START_DATE_TIME))

    request_id = rest_server.get_next_request_id()

    response = dtc_client.request_response(
        request_id,
        HistoricalOrderFillsRequest(
            request_id=request_id,
            trade_account=trade_account,
            number_of_days=number_of_days,
            start_date_time=start_date_time
        )
    )
    return jsonify(response)


@app.route(API.API_PREFIX + API.SECURITY_DEFINITION)
def security_definition():
    logging.info('Security definition request')

    logging.info('dtc_client: %s' % dtc_client)

    symbol = rest_server.get_query_param(SYMBOL)
    exchange = rest_server.get_query_param(EXCHANGE, required=False)
    request_id = rest_server.get_next_request_id()

    response = dtc_client.request_response(
        request_id,
        SecurityDefinitionForSymbolRequest(
            request_id=request_id,
            symbol=symbol,
            exchange=exchange
        )
    )
    return jsonify(response)


@app.route(API.API_PREFIX + API.TRADE_ACCOUNTS)
def trade_accounts():
    request_id = rest_server.get_next_request_id()

    response = dtc_client.request_response(
        request_id,
        TradeAccountsRequest(
            request_id=request_id,
        )
    )
    return jsonify(response)


class RESTServer:
    def __init__(self):
        global rest_server
        rest_server = self
        self.request_id = 0
        self.request_id_lock = Lock()

    def get_next_request_id(self):
        self.request_id_lock.acquire()
        self.request_id += 1
        request_id = self.request_id
        self.request_id_lock.release()
        return request_id

    def start(self, _dtc_client, _rest_port):
        logging.info('Starting REST Server')
        global dtc_client
        dtc_client = _dtc_client

        from gevent import pywsgi
        from geventwebsocket.handler import WebSocketHandler
        server = pywsgi.WSGIServer(('0.0.0.0', _rest_port), app, handler_class=WebSocketHandler)
        server.serve_forever()

    @staticmethod
    def get_query_param(variable, required=True):
        value = request.args.get(variable)
        if not value and required:
            raise InvalidArgumentsError('%s must be specified' % variable)
        return value













