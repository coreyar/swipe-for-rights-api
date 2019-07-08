from helpers.serializers import BaseSerializer
from .models import Vote


class VoteSerializer(BaseSerializer):

    class Meta:
        model = Vote
        fields = []
