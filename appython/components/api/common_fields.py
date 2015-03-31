'''
The fields supported by Flask-Restful: String, FormattedString, Url, DateTime,
Float, Integer, Arbitrary, Nested, List, Raw, Boolean, Fixed, and Price.
'''

from flask.ext.restful import fields

'''
ID-related fields. We convert them to strings to avoid overflows in some
languages (i.e. Java.)
'''


class IdField(fields.Raw):
    def output(self, key, obj):
        if getattr(obj, 'key', None) is None:
            return None
        return unicode(obj.key.id())

class ParentIdField(fields.Raw):
    def output(self, key, obj):
        if getattr(obj, 'key', None) is None:
            return None
        return unicode(obj.key.parent().id())

'''
When we don't want to show the content of a field, and instead we only want to
show if the field is set or not. Used in google_client_secret for example.
'''

class IsSetField(fields.Raw):
    def output(self, key, obj):
        return True if getattr(obj, key, None) else False
