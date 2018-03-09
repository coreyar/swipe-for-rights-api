import typing

from apistar import (
    Response,
    annotate,
)
from apistar.exceptions import NotFound
from apistar.interfaces import Auth

from swipe_for_rights_api.helpers import stringify_all_dates
from swipe_for_rights_api.database.models.votes import UserVoteModel
from .types import UserVoteType


def get_votes(auth: Auth) -> typing.List[UserVoteType]:
    """Get all of the authenticated User's votes."""
    return UserVoteModel.objects(user_id=auth.user['id']).to_json()


def get_vote(auth: Auth, bill_id: str) -> UserVoteType:
    """Get a User's vote for a Bill.

    This 404s if the User has not set a Vote for the Bill yet.
    """
    try:
        vote = UserVoteModel.objects(
            user_id=auth.user['id'],
            bill_id=bill_id,
        ).get()
        return vote.to_json()
    except UserVoteModel.DoesNotExist:
        raise NotFound()


def set_vote(auth: Auth, vote: UserVoteType):
    """Set a User's vote for a Bill.

    The existing UserVote for the Bill will be overwritten, if set.
    """
    try:
        vote_model = UserVoteModel.objects(
            user_id=auth.user['id'],
            bill_id=vote['bill_id'],
        ).get()
    except UserVoteModel.DoesNotExist:
        vote_model = UserVoteModel(
            user_id=auth.user['id'],
            bill_id=vote['bill_id'],
        )

    vote_model.supports = vote['supports']
    vote_model.save()

    return Response(status=201)
