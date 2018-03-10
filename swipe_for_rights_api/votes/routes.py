from apistar import Route

from . import controllers


vote_routes = [
    Route('/', 'POST', controllers.set_vote),
]
