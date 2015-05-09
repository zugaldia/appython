from flask.ext.restful import reqparse

'''
User endpoint
'''

user_setup_request = reqparse.RequestParser()
user_setup_request.add_argument('password', type=unicode)
