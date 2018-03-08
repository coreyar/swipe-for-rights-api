from requests_jwt import JWTAuth as RequestsJWTAuth

from swipe_for_rights_api.settings import settings


def get_jwt_auth(user_id, username='madeup'):
    """Returns a Requests and API Star compatible JWT Auth instance.

    The Requests compatibility come from populating requests_jwt, which
    implements the `Requests Auth interface <>`_, with the headers, secrets,
    and payload that apistar_jwt expects.

    For now we haven't implemented username anywhere, so it is set to a
    'madeup' value by default.

    .. _Request Auth interface: http://docs.python-requests.org/en/master/user/authentication/#new-forms-of-authentication
    """
    auth = RequestsJWTAuth(
        settings['JWT']['SECRET'],
        # By default, requests_jwt uses "Authorization: JWT %s", apistar_jwt
        # expects the recommended "Bearer %s"
        header_format='Bearer %s'
    )
    auth.add_field(settings['JWT'].get('ID', 'id'), user_id)
    auth.add_field(settings['JWT'].get('USERNAME', 'username'), username)
    return auth
