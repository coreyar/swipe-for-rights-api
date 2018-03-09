from apistar import Route

from . import controllers


vote_routes = [
    Route('/', 'GET', controllers.get_votes),
    Route('/', 'POST', controllers.set_vote),
    Route('/{bill_id}', 'GET', controllers.get_vote),
]
