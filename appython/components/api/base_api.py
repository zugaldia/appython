from appython.components.api.api_exception import ApiException
from appython.components.api.api_status import ApiStatus
from flask import request
from flask.ext.restful import Resource

# import logging


class BaseApi(Resource):
    def __init__(self):
        # Defaults
        self._data = {}
        self._code = ApiStatus.OK
        self._message = 'OK'

        # If we add custom headers we need to handle options() too. See:
        # https://developer.mozilla.org/en-US/docs/HTTP/Access_control_CORS#Preflighted_requests
        self._headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS'}

    '''
    HTTP methods
    We're ignoring: head, trace, and patch
    '''

    def get(self, action):
        return self._process_method(request_type='get', action=action)

    def post(self, action):
        return self._process_method(request_type='post', action=action)

    def put(self, action):
        return self._process_method(request_type='put', action=action)

    def delete(self, action):
        return self._process_method(request_type='delete', action=action)

    def options(self, action):
        # Required by preflighted requests, see link in __init__() above
        return self.get_response()

    '''
    Main handler
    '''

    def _process_method(self, request_type, action):
        # No action
        if not action:
            self.set_message(message='Please include an action in your request.')
            self.set_code(code=ApiStatus.BAD_REQUEST)
            return self.get_response()

        # All good
        method_name = '%s_%s' % (request_type, action)
        if not action.startswith('_') and hasattr(self, method_name):
            return getattr(self, method_name)()

        # Unknown action
        self.set_message(
            message='Unknown action %s (%s) in %s.'
            % (action, request_type.upper(), self.__class__.__name__))
        self.set_code(code=ApiStatus.NOT_FOUND)
        return self.get_response()

    '''
    Utils to build the response
    '''

    def set_data(self, data):
        if not isinstance(data, dict):
            raise ApiException('BaseApi: `data` must be a dict.')
        for key in data.keys():
            if key.startswith('status'):
                raise ApiException('BaseApi: `status*` is a reserved key.')
        self._data = data

    def set_code(self, code):
        self._code = code

    def set_message(self, message):
        self._message = message

    def get_response(self):
        data = self._data
        data['status_code'] = self._code
        data['status_message'] = self._message
        return data, self._code, self._headers
