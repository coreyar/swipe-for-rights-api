from mongoengine import (
    BooleanField,
    Document,
    ReferenceField,
    StringField,
)
from mongoengine.document import BaseDocument


class UserVoteModel(Document):
    """A record of a User's support of a Bill"""
    # A reference to a User
    user_id = StringField(required=True)
    # By id - we're not storing Bills yet
    bill_id = StringField(required=True)
    supports = BooleanField(required=True)
