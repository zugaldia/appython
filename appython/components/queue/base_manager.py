from google.appengine.api import taskqueue
import json
import pickle

import logging


class BaseManager(object):

    '''
    Utils to encode and decode
    '''

    @staticmethod
    def encode(data):
        data = data or {}
        result = pickle.dumps(data)
        return result

    @staticmethod
    def decode(data):
        result = pickle.loads(data)
        return result or {}

    '''
    All tasks launched from here

    We use dry_run when we don't actually want to launch the task, this
    happens, for example, when we're in development mode and the queues
    are not set up in the API module.
    '''

    @classmethod
    def launch_task(cls, queue_name, data=None, countdown_s=None, dry_run=False):
        if dry_run:
            message = '[launch_task] {} ({}): {}'.format(queue_name, countdown_s, json.dumps(data))
            logging.info(message)
            return
        return taskqueue.add(
            queue_name=queue_name,
            method='POST',
            params={'data': cls.encode(data)},
            countdown=countdown_s)
