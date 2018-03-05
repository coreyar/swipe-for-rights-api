from datetime import (
    date,
    timedelta,
)
import json

from apistar import annotate, Response
from apistar.interfaces import Auth
from apistar_jwt.authentication import JWTAuthentication
import pyopenstates

from swipe_for_rights_api.helpers import stringify_all_dates


# @annotate(authentication=[JWTAuthentication()])
def fetchBills(auth: Auth):
    # state = auth.get('state', 'TN')
    state = 'TN'
    # Paginate based on date
    updated_since = str(date.today() - timedelta(days=30))
    bills = pyopenstates.search_bills(state=state, updated_since=updated_since)
    for b in bills:
        stringify_all_dates(b)
    print(bills)
    return Response(bills, status=200)
