import factory

from swipe_for_rights_api.database.models.votes import VoteModel


class VoteFactory(factory.mongoengine.MongoEngineFactory):
    class Meta:
        model = VoteModel
    bill_id = factory.Sequence(lambda n: 'BH{}'.format(n))
    supports = True
