from flask.ext.restful import reqparse

'''
For boolean requests, when we define the type as bool (like
bool_request below), the value is always true as long as it's set,
even if we set it to "false". For that reason, it's probably easier to
use a string_request and check if the value is in this list:

    flag = args.get('flag') in TRUE_VALUES

We also include the unicode character for the check mark (cool, right?)
http://en.wikipedia.org/wiki/Check_mark#Unicode
'''

TRUE_VALUES = ['true', 'True', 'TRUE', '1', u'\u2713']

'''
Requests
'''

string_request = reqparse.RequestParser()
string_request.add_argument('text', type=unicode)

int_request = reqparse.RequestParser()
int_request.add_argument('number', type=int)

float_request = reqparse.RequestParser()
float_request.add_argument('number', type=float)

long_request = reqparse.RequestParser()
long_request.add_argument('number', type=long)

bool_request = reqparse.RequestParser()
bool_request.add_argument('flag', type=bool)
