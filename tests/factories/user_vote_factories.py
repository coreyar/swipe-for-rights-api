import factory

from swipe_for_rights_api.database.models.votes import UserVoteModel
from .user_factories import UserFactory


class UserVoteFactory(factory.mongoengine.MongoEngineFactory):
    class Meta:
        model = UserVoteModel

    class Params:
        # Guarantees ``user_id`` is a real user. We can't put directly in the
        # factory because ``user`` isn't a valid object field.
        user = factory.SubFactory(UserFactory)

    user_id = factory.LazyAttribute(lambda self: str(self.user.id))
    bill_id = factory.Sequence(lambda n: 'BH{}'.format(n))
    supports = True
