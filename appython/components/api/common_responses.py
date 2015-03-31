from flask.ext.restful import fields, marshal

class StringResponse(object):
    def __init__(self, text):
        self.text = text

    def to_api(self):
        model_fields = {'text': fields.String}
        return marshal(self, model_fields)
