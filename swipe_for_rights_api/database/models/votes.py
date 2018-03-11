from mongoengine import (
    BooleanField,
    EmbeddedDocument,
    StringField,
)


class VoteModel(EmbeddedDocument):
    """A record of a User's support of a Bill"""
    # By id - we're not storing Bills yet
    bill_id = StringField(required=True)
    # True if they support, False if not
    supports = BooleanField(required=True)
