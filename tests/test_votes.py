import json

from apistar.test import TestClient

from app import app

from swipe_for_rights_api.database.models.votes import UserVoteModel
from swipe_for_rights_api.votes.types import UserVoteType
from .auth_utils import get_jwt_auth
from .factories.user_factories import UserFactory
from .factories.user_vote_factories import UserVoteFactory


def test_set_vote(client):
    """Writing out a UserVote returns a 200 creates a database record."""
    vote_params = dict(bill_id='AB111', supports='true')
    user = UserFactory()
    # The ObjectId here has to explicitly be cast to a str
    user_id = str(user.id)
    response = client.post(
        '/votes/',
        data=vote_params,
        auth=get_jwt_auth(user_id),
    )
    assert response.status_code == 201


def test_get_vote(client):
    """Get out a UserVote by ``bill_id``."""
    vote = UserVoteFactory()
    response = client.get(
        '/votes/{vote.bill_id}'.format(vote=vote),
        auth=get_jwt_auth(vote.user_id),
    )
    assert response.status_code == 200
    assert UserVoteModel.from_json(response.json()) == vote


def test_get_votes(client):
    """Get all of User's UserVotes."""
    user = UserFactory()
    votes = [
        UserVoteFactory(user=user),
        UserVoteFactory(user=user),
        UserVoteFactory(user=user),
        UserVoteFactory(user=user),
    ]
    response = client.get(
        '/votes/',
        auth=get_jwt_auth(str(user.id)),
    )
    assert response.status_code == 200
    assert UserVoteModel.objects.from_json(response.json()) == votes
