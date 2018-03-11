from apistar.authentication import Unauthenticated
from apistar import http
from apistar.types import Settings
from apistar_jwt.authentication import JWTAuthentication
from apistar_jwt.exceptions import AuthenticationFailed


class Issue8JWTAuthentication(JWTAuthentication):
    """JWTAuthentication with a fix for apistar_jwt#8.

    Instead of raising an AuthenticationFailed exception, it returns None.
    """
    def authenticate(self, authorization: http.Header, settings: Settings):
        try:
            return super().authenticate(authorization, settings)
        except AuthenticationFailed:
            return None


class UnAuthentication:
    """Authentication that always returns an Unauthenticated instance."""
    def authenticate(self):
        """Returns Unauthenticated()"""
        return Unauthenticated()
