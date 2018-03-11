from mongoengine import (
    Document,
    StringField,
)
from mongoengine.document import BaseDocument

class UserModel(Document):
    email = StringField(required=True)
    password = StringField(required=True)
    street_address = StringField()
    locality = StringField()
    region = StringField()
    postal_code = StringField()
