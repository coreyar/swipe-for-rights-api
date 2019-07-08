from helpers.serializers import BaseSerializer
from .models import Bill


class BillSerializer(BaseSerializer):

    class Meta:
        model = Bill
        fields = []
