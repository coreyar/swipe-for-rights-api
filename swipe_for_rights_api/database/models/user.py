from mongoengine import (
    Document,
    EmbeddedDocumentListField,
    StringField,
)

from .votes import VoteModel


class UserModel(Document):
    email = StringField(required=True)
    password = StringField(required=True)
    street_address = StringField()
    locality = StringField()
    region = StringField()
    postal_code = StringField()
    votes = EmbeddedDocumentListField(document_type=VoteModel)
