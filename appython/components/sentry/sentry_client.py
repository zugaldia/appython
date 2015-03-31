'''
See: http://raven.readthedocs.org/en/latest/integrations/flask.html
'''

from raven.contrib.flask import Sentry
import traceback

import logging


class SentryClient(object):
    def __init__(self, sentry_dsn=None):
        # In development mode, we can pass a None value for the DSN and
        # instead of sending the reports to Sentry, we just use logging to
        # show it in the server log.
        self._sentry_dsn = sentry_dsn
        self._client = Sentry(dsn=sentry_dsn)

    def init_app(self, app):
        if self._sentry_dsn is None:
            logging.info('[mock] SentryClient.init_app')
            return
        self._client.init_app(app=app)

    def capture_exception(self):
        if self._sentry_dsn is None:
            logging.error('[mock] SentryClient.capture_exception')
            traceback.print_exc()
            return
        self._client.captureException()

    def capture_message(self, message):
        if self._sentry_dsn is None:
            logging.error('[mock] SentryClient.capture_message')
            logging.error(message)
            return
        self._client.captureMessage(message)
