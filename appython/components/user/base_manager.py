'''
Some functions useful for user management
'''

from appython.utils.generators import generate_key
from appython.utils.generators import generate_secret
from werkzeug import security


class BaseManager(object):

    '''
    Email related
    '''

    @staticmethod
    def prepare_email(email):
        return email.lower().strip()

    '''
    Password security
    http://flask.pocoo.org/snippets/54/
    http://werkzeug.pocoo.org/docs/utils/#module-werkzeug.security
    '''

    @staticmethod
    def get_password_hash(password):
        return security.generate_password_hash(
            password=password)

    @staticmethod
    def check_password_hash(self, password_hash, password):
        return security.check_password_hash(
            pwhash=password_hash, password=password)

    '''
    API keys
    '''

    @staticmethod
    def generate_api_key():
        return generate_key()

    '''
    Create a random password
    '''

    @staticmethod
    def generate_password():
        return generate_secret()
