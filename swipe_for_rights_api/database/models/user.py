import typing

from apistar import typesystem
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



class UserType(typesystem.Object):
    properties = {
        'email': typesystem.string(max_length=100),  # Use lowercase functions for inline declarations.
        'password': typesystem.string(max_length=100),
        'street_address': typesystem.string(max_length=100),
        'locality': typesystem.string(max_length=100),
        'region': typesystem.string(max_length=2),
        'postal_code': typesystem.string(max_length=5),
    }

# array of fields [{type, required, max_length}]

def model_type(field_type, required):
    if field_type == 'string':
        return StringField(required=required)

def typesystem_type(field_type, max_length):
    if field_type == 'string':
        return typesystem.string(max_length=max_length)

def mongo_star(fields):
    class TypeObject(typesystem.Object):
        properties = {}

    class MongoDocument(Document):
        pass
        for field in fields:
            locals()[field['name']] = model_type(field['type'], field['required'])

    for field in fields:
        TypeObject.properties[field['name']] = typesystem_type(field['type'], field['max_length'])

    class DocumentWithType(object):
        model = MongoDocument
        types = TypeObject

    return DocumentWithType


user_fields = [
    {'name': 'email', 'type': 'string', 'max_length': 100, 'required': True },
    {'name': 'password', 'type': 'string', 'max_length': 100, 'required': True },
    {'name': 'street_address', 'type': 'string', 'max_length': 100, 'required': True },
    {'name': 'locality', 'type': 'string', 'max_length': 100, 'required': True },
    {'name': 'region', 'type': 'string', 'max_length': 2, 'required': True },
    {'name': 'postal_code', 'type': 'string', 'max_length': 5, 'required': True },
]

User = mongo_star(user_fields)
