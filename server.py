#!/usr/bin/python3


# Python libraries
import json
import sys
# 3rd party libraries
from flask import Flask, render_template, request, jsonify
# Internal files
from exceptions import *
import roulette


# HTML files
INDEX = 'index'
HTML_INDEX = INDEX + '.html'
# Required parameters
PARAM_BET = 'bet'
PARAM_WAGER = 'wager'
API_REQ_PARAMS = {PARAM_BET, PARAM_WAGER}
# HTTP statuses
HTTP_STATUS_OK = 200
HTTP_STATUS_BAD_REQUEST = 400
HTTP_STATUS_INTERNAL_ERROR = 500
# Error messages
ERROR_MISSING_PARAM = 'Missing parameter: %s'
ERROR_INVALID_NUMBER = 'Error generating number'
ERROR_INVALID_BET = 'Invalid bet: %s'
ERROR_INVALID_WAGER = 'Invalid wager: %s'
ERROR_UNSPECIFIED = 'Error fulfilling request'
# Defaults
DEFAULT_BET = 'even'
DEFAULT_WAGER = '200'
# Flask instantiation
APP = Flask(__name__)
APP.config['JSON_SORT_KEYS'] = False


# Displays home page
@APP.route('/', methods=['GET'])
def home():
    req_display = json.dumps(roulette.play(DEFAULT_BET, DEFAULT_WAGER))
    return render_template(HTML_INDEX, req_display=req_display)


# API request to play roulette
@APP.route('/api/play', methods=['GET'])
def api_play():
    return play_handler(request.args)


def play_handler(payload):
    is_valid, error_msg = validate_params(payload)
    if not is_valid:
        print('Invalid payload: %s' % error_msg)
        return generate_error_response(error_msg), HTTP_STATUS_BAD_REQUEST, None
    try:
        response = roulette.play(payload[PARAM_BET], payload[PARAM_WAGER])
        print('Successful game. Response:\n%s' % response)
        return jsonify(response), HTTP_STATUS_OK, None
    except InvalidRollNumberException as e:
        print('Exception: %s' % e)
        return generate_error_response(ERROR_INVALID_NUMBER), HTTP_STATUS_INTERNAL_ERROR, None
    except InvalidBetException as e:
        print('Exception: %s' % e)
        return generate_error_response(ERROR_INVALID_BET % payload[PARAM_BET]), HTTP_STATUS_BAD_REQUEST, None
    except InvalidWagerException as e:
        print('Exception: %s' % e)
        return generate_error_response(ERROR_INVALID_BET % payload[PARAM_WAGER]), HTTP_STATUS_BAD_REQUEST, None
    except Exception as e:
        print('Unspecified exception: %s' % e)
        return generate_error_response(ERROR_UNSPECIFIED), HTTP_STATUS_INTERNAL_ERROR, None


# Validates the request parameters. Returns tuple: (if valid params, error message)
def validate_params(payload: dict):
    print('Payload: %s' % payload)
    for param in API_REQ_PARAMS:
        if param not in payload:
            return False, ERROR_MISSING_PARAM % param
    return True, ''


def generate_error_response(msg):
    return jsonify({
        'success': False,
        'message': msg
    })


# todo: make this take in GET result params to display them on page
def get_attributes():
    return dict()


if __name__ == '__main__':
    APP.run(debug='debug' in sys.argv, host='127.0.0.1', port=5001)
