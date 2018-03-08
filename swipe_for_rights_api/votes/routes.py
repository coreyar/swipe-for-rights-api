from apistar import Route

from . import controllers


vote_routes = [
    Route('/{user_id}/', 'GET', controllers.get_votes),
    Route('/{user_id}/{bill_id}', 'GET', controllers.get_vote),
    Route('/{user_id}/{bill_id}/{supports}', 'POST', controllers.set_vote),
]
