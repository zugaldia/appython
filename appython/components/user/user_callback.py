'''
This sets the callback for reloading a user from the session. The function
you set should take a user ID (a unicode) and return a user object, or
None if the user does not exist.
'''

from google.appengine.ext import ndb


def user_callback(user_id):
    # Because we are always provided an unicode here, we use the urlsafe()
    # method to identify the users, instead of the usual ID.
    user_key = ndb.Key(urlsafe=user_id)
    user_model = user_key.get()
    return user_model
