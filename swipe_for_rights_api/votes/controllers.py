import typing

from apistar import (
    Response,
    annotate,
)
from apistar.exceptions import NotFound

from swipe_for_rights_api.helpers import stringify_all_dates
from swipe_for_rights_api.database.models.votes import UserVoteModel
from swipe_for_rights_api.settings import DEFAULT_PERMISSIONS
from .types import UserVoteType
from .permissions import (
    UserVoteRead,
    UserVoteWrite,
)


@annotate(
    permissions=(*DEFAULT_PERMISSIONS, UserVoteRead(),)
)
def get_votes(user_id: str) -> typing.List[UserVoteType]:
    """Get all of a User's votes."""
    return UserVoteModel.objects(user_id=user_id).to_json()


@annotate(
    permissions=(*DEFAULT_PERMISSIONS, UserVoteRead(),)
)
def get_vote(user_id: str, bill_id: str) -> UserVoteType:
    """Get a User's vote for a Bill.

    This 404s if the User has not set a Vote for the Bill yet.
    """
    try:
        return UserVoteModel.objects(
            user_id=user_id, bill_id=bill_id
        ).get().to_json()
    except UserVoteModel.DoesNotExist:
        raise NotFound()


@annotate(
    permissions=(*DEFAULT_PERMISSIONS, UserVoteWrite(),)
)
def set_vote(user_id: str, bill_id: str, supports: bool):
    """Set a User's vote for a Bill.

    The existing UserVote for the Bill will be overwritten, if set.
    """
    try:
        vote = UserVoteModel.objects(user_id=user_id, bill_id=bill_id).get()
    except UserVoteModel.DoesNotExist:
        vote = UserVoteModel(user_id=user_id, bill_id=bill_id)

    vote.supports = supports
    vote.save()

    return Response(content={'id': str(vote.id)}, status=201)
