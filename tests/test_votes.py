import json

from apistar.test import TestClient

from app import app

from swipe_for_rights_api.database.models.votes import UserVoteModel
from .auth_utils import get_jwt_auth
from .factories.user_factories import UserFactory
from .factories.user_vote_factories import UserVoteFactory


def test_set_vote(client):
    """Writing out a UserVote returns a 200 creates a database record."""
    user = UserFactory()
    # The ObjectId here has to explicitly be cast to a str
    user_id = str(user.id)
    response = client.post(
        '/votes/{}/AB111/1'.format(user_id),
        auth=get_jwt_auth(user_id),
    )
    assert response.status_code == 201


def test_get_vote(client):
    """Get out a UserVote by ``bill_id``."""
    vote = UserVoteFactory()
    auth = get_jwt_auth(vote.user_id)
    response = client.get(
        '/votes/{vote.user_id}/{vote.bill_id}'.format(vote=vote),
        auth=auth,
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
    auth = get_jwt_auth(str(user.id))
    response = client.get(
        '/votes/{user.id}/'.format(user=user),
        auth=auth,
    )
    assert response.status_code == 200
    assert UserVoteModel.objects.from_json(response.json()) == votes
