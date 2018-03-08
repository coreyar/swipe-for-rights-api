import factory

from swipe_for_rights_api.database.models.user import UserModel


class UserFactory(factory.mongoengine.MongoEngineFactory):
    class Meta:
        model = UserModel

    email = 'usa@usa.usa'
    password = '234asdf291'
