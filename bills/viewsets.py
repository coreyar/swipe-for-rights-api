from datetime import (
    date,
    timedelta,
)
import pyopenstates

from helpers.utils import stringify_all_dates
from helpers.viewsets import BaseViewSet

from .serializers import BillSerializer
from .models import Bill


class BillViewSet(BaseViewSet):
    """
        Endpoints:\n
            GET    -   /bills/
    """

    serializer_class = BillSerializer
    queryset = Bill.objects.filter()

    def list(self, request):
        state = 'TN'
        updated_since = str(date.today() - timedelta(days=1))
        bills = pyopenstates.search_bills(state=state, updated_since=updated_since)
        for b in bills:
            stringify_all_dates(b)
        return self.respond(raw=bills, status=200)
