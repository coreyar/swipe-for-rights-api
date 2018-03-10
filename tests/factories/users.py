import factory

from swipe_for_rights_api.database.models.user import UserModel

from .votes import VoteFactory

class UserFactory(factory.mongoengine.MongoEngineFactory):
    class Meta:
        model = UserModel

    email = 'usa@usa.usa'
    password = '234asdf291'
    votes = factory.List([
        factory.SubFactory(VoteFactory),
        factory.SubFactory(VoteFactory),
        factory.SubFactory(VoteFactory),
    ])
