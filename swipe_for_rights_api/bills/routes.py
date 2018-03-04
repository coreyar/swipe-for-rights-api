from apistar import Route

from .controllers import fetchBills


bill_routes = [
    Route('/', 'GET', fetchBills),
]
