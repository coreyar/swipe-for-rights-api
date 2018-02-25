import base64
import os
from apistar import http
from apistar.authentication import Authenticated
import pyopenstates

pyopenstates.set_api_key(os.environ['OPEN_STATES_API_KEY'])

settings = {
    'JWT': {
        'SECRET': os.environ['SECRET_KEY']
    }
}