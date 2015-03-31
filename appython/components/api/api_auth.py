'''
A decorator for API methods that require some kind of authentication. If the
method doesn't require authentication, this decorator desn't need to be applied.
'''

from appython.components.api.api_status import ApiStatus
from flask_login import current_user

# import logging


def api_auth(login_required=False, admin_required=False):
    def dec(func):
        def f2(*args, **kwds):
            # Check authentication. Flask-Login tracks both API *and* web
            # requests. We also need to check is_active(), I thought
            # Flask-Login would take care of this but apparently it only
            # works for the login_user() method.
            if login_required or admin_required:
                # Not authenticated
                if not current_user.is_authenticated():
                    args[0].set_code(code=ApiStatus.UNAUTHORIZED)
                    args[0].set_message(message='Please login first.')
                    return args[0].get_response()
                # Inactive account
                if not current_user.is_active():
                    args[0].set_code(code=ApiStatus.UNAUTHORIZED)
                    args[0].set_message(message='Your account is currently inactive.')
                    return args[0].get_response()
                # Authenticated but not admin
                if admin_required and not current_user.is_admin:
                    args[0].set_code(code=ApiStatus.FORBIDDEN)
                    args[0].set_message(message='Please login with your admin credentials.')
                    return args[0].get_response()

            # All good otherwise
            return func(*args, **kwds)
        return f2
    return dec
