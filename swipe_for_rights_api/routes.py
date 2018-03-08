from apistar import (
    Include,
    Route,
)
from apistar.handlers import (
    docs_urls,
    static_urls,
)

from .annotations import public
from .auth.routes import auth_routes
from .bills.routes import bill_routes
from .votes.routes import vote_routes


@public()
def welcome(name=None):
    if name is None:
        return {'message': 'Welcome to API Star!'}
    return {'message': 'Welcome to API Star, %s!' % name}

routes = [
    Include('/', auth_routes),
    Include('/docs', docs_urls),
    Include('/bills', bill_routes),
    Include('/votes', vote_routes),
    Include('/static', static_urls),
]
