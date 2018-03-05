from apistar import (
    Include,
    Route,
)
from apistar.handlers import (
    docs_urls,
    static_urls,
)


from .auth.routes import auth_routes
from .bills.routes import bill_routes


def welcome(name=None):
    if name is None:
        return {'message': 'Welcome to API Star!'}
    return {'message': 'Welcome to API Star, %s!' % name}

routes = [
    Route('/', 'GET', welcome),
    Include('/', auth_routes),
    Include('/docs', docs_urls),
    Include('/bills', bill_routes),
    Include('/static', static_urls),
]
