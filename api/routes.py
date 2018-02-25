from apistar import Include
from .auth.routes import auth_routes
from .bills.routes import bill_routes
routes = [
    Include('/', auth_routes),
    Include('/bills', bill_routes),
]