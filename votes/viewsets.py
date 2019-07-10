from helpers.viewsets import BaseAuthViewSet
from .serializers import VoteSerializer
from .models import Vote


class VoteViewSet(BaseAuthViewSet):
    """
        Endpoints:\n
            POST    -   /vote/
    """

    serializer_class = VoteSerializer
    queryset = Vote.objects.filter()

    def update(self, request, pk=None):
        """Set a User's vote for a Bill.

        The existing UserVote for the Bill will be overwritten, if set.
        """
        supports = request.data.get('supports', False)
        user = request.user
        if user:
            try:
                vote = next(vote for vote in user.votes if vote.bill_id == pk)
                vote.supports = supports
            except StopIteration:
                vote = Vote.objects.create(bill_id=pk, supports=supports)
                user.votes.append(vote)
            user.save()
            return self.respond(status=201)
        return self.respond(status=412)
