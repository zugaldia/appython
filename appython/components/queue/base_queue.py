from appython.components.queue.base_manager import BaseManager
from flask import request
from flask.views import MethodView

# import logging


class BaseQueue(MethodView):
    def _is_legit(self):
        is_queue_task = 'X-Appengine-Queuename' in request.headers
        return is_queue_task

    def _initialize_data(self):
        self.data = BaseManager.decode(request.form.get('data'))
