import os

from apistar.permissions import IsAuthenticated
from apistar_jwt.authentication import JWTAuthentication

# Public endpoints don't require any permissions
PUBLIC_PERMISSIONS = tuple()


settings = {
    'AUTHENTICATION': (
        JWTAuthentication(),
    ),
    'PERMISSIONS': (
        IsAuthenticated(),
    ),
    'JWT': {
        'SECRET': os.environ['SWIPE_FOR_RIGHTS_JWT_SECRET_KEY']
    },
}
