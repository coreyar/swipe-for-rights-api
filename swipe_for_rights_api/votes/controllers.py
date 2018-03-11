import typing

from apistar import (
    Response,
    annotate,
)
from apistar.exceptions import NotFound
from apistar.interfaces import Auth
from mongoengine.errors import DoesNotExist

from swipe_for_rights_api.helpers import stringify_all_dates
from swipe_for_rights_api.database.models.user import UserModel
from swipe_for_rights_api.database.models.votes import VoteModel
from .types import UserVoteType


def set_vote(auth: Auth, vote: UserVoteType):
    """Set a User's vote for a Bill.

    The existing UserVote for the Bill will be overwritten, if set.
    """
    user = UserModel.objects(id=auth.user['id']).get()
    try:
        user.votes.get(
            bill_id=vote['bill_id']
        ).update(
            supports=vote['supports']
        )
    except DoesNotExist:
        user.votes.create(
            bill_id=vote['bill_id'],
            supports=vote['supports']
        )
    user.save()

    return Response(status=201)
