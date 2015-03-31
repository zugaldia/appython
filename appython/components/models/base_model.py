from appython.components.api.common_fields import IdField
from flask.ext.restful import fields
from google.appengine.ext import ndb


class BaseModel(ndb.Model):
    # Automatically track create and update time. App Engine clock times are
    # always expressed in coordinated universal time (UTC).
    created = ndb.DateTimeProperty(auto_now_add=True)
    updated = ndb.DateTimeProperty(auto_now=True)

    # Has this item been marked for deletion?
    deleted = ndb.BooleanProperty(default=False)

    def get_id(self):
        return self.key.id() if self.key is not None else None

    def get_basic_fields(self):
        # Basic fields common to all models
        basic_fields = {
            'id': IdField,
            'created': fields.DateTime,
            'updated': fields.DateTime,
            'deleted': fields.Boolean}
        return basic_fields
