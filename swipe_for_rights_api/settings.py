import base64
import os

from apistar import http
from apistar.authentication import Authenticated
import pyopenstates


settings = {
    'JWT': {
        'SECRET': os.environ['SWIPE_FOR_RIGHTS_JWT_SECRET_KEY']
    }
}
