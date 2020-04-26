import logging

from flask import Flask, request, jsonify
from flask_classful import FlaskView, route
from threading import Lock

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

PRETTY = True

dtc_client = None

TRADE_ACCOUNT = 'TradeAccount'
NUMBER_OF_DAYS = 'NumberOfDays'
START_DATE_TIME = 'StartDateTime'
SYMBOL = 'Symbol'
EXCHANGE = 'Exchange'


@app.errorhandler(InvalidArgumentsError)
def handle_invalid_arguments_error(error):
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


@app.errorhandler(RequestTimeoutError)
def handle_request_timeout(error):
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


class RESTServer(FlaskView):
    def __init__(self):
        self.request_id = 0
        self.request_id_lock = Lock()

    def get_next_request_id(self):
        self.request_id_lock.acquire()
        self.request_id += 1
        request_id = self.request_id
        self.request_id_lock.release()
        return request_id

    def start(self, _dtc_client, _rest_port):
        global dtc_client
        dtc_client = _dtc_client
        app.run(port=_rest_port)

    def get_query_param(self, variable, required=True):
        value = request.args.get(variable)
        if not value and required:
            raise InvalidArgumentsError('%s must be specified' % variable)
        return value

    @route(API.ACCOUNT_BALANCE)
    def account_balance(self):
        request_id = self.get_next_request_id()
        response = dtc_client.request_response(
            request_id,
            AccountBalanceRequest(
                request_id=request_id
            )
        )
        return jsonify(response)

    @route(API.CURRENT_POSITIONS)
    def current_positions(self):
        request_id = self.get_next_request_id()
        response = dtc_client.request_response(
            request_id,
            CurrentPositionsRequest(
                request_id=request_id
            )
        )
        return jsonify(response)

    @route(API.EXCHANGE_LIST)
    def exchange_list(self):
        request_id = self.get_next_request_id()
        response = dtc_client.request_response(
            request_id,
            ExchangeListRequest(
                request_id=request_id
            )
        )
        return jsonify(response)

    @route(API.HISTORICAL_ACCOUNT_BALANCES)
    def historical_account_balance(self):
        trade_account = self.get_query_param(TRADE_ACCOUNT)
        start_date_time = self.get_query_param(START_DATE_TIME, required=False)
        request_id = self.get_next_request_id()

        response = dtc_client.request_response(
            request_id,
            HistoricalAccountBalancesRequest(
                request_id=request_id,
                trade_account=trade_account,
                start_date_time=start_date_time
            )
        )
        return jsonify(response)

    @route(API.HISTORICAL_ORDER_FILLS)
    def historical_order_fills(self):
        trade_account = self.get_query_param(TRADE_ACCOUNT)
        number_of_days = self.get_query_param(NUMBER_OF_DAYS, required=False)
        start_date_time = self.get_query_param(START_DATE_TIME, required=False)
        if not number_of_days and not start_date_time:
            raise InvalidArgumentsError('Either %s or %s must be specified' % (NUMBER_OF_DAYS, START_DATE_TIME))

        request_id = self.get_next_request_id()

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

    @route(API.SECURITY_DEFINITION)
    def security_definition(self):
        symbol = self.get_query_param(SYMBOL)
        exchange = self.get_query_param(EXCHANGE, required=False)
        request_id = self.get_next_request_id()

        response = dtc_client.request_response(
            request_id,
            SecurityDefinitionForSymbolRequest(
                request_id=request_id,
                symbol=symbol,
                exchange=exchange
            )
        )
        return jsonify(response)

    @route(API.TRADE_ACCOUNTS)
    def trade_accounts(self):
        request_id = self.get_next_request_id()

        response = dtc_client.request_response(
            request_id,
            TradeAccountsRequest(
                request_id=request_id,
            )
        )
        return jsonify(response)


RESTServer.register(app, route_base=API.API_PREFIX)












