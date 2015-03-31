from google.appengine.api import taskqueue
import pickle

# import logging


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
    '''

    @classmethod
    def launch_task(cls, queue_name, data=None, countdown_s=None):
        return taskqueue.add(
            queue_name=queue_name,
            method='POST',
            params={'data': cls.encode(data)},
            countdown=countdown_s)
