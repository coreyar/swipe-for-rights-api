import json

from .auth_utils import get_jwt_auth
from .factories.users import UserFactory


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
