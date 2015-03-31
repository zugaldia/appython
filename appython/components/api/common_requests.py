from flask.ext.restful import reqparse

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
