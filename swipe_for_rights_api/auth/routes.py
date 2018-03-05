from apistar import Route

from .controllers import login, signup, me


auth_routes = [
    Route('login', 'POST', login),
    Route('signup', 'POST', signup),
    Route('me', 'POST', me),
]
