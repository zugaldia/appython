from flask import request
from flask.views import MethodView

# import logging

class BaseCron(MethodView):
    def _is_legit(self):
        is_queue_task = (request.headers.get('X-Appengine-Cron') == 'true')
        return is_queue_task
