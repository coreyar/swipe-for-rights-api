import os

from apistar.permissions import IsAuthenticated

from .authentication import (
    Issue8JWTAuthentication,
    UnAuthentication
)


# Public endpoints don't require any permissions
PUBLIC_PERMISSIONS = tuple()


settings = {
    'AUTHENTICATION': (
        Issue8JWTAuthentication(),
    ),
    'PERMISSIONS': (
        IsAuthenticated(),
    ),
    'JWT': {
        'SECRET': os.environ['SWIPE_FOR_RIGHTS_JWT_SECRET_KEY']
    },
}
