from rest_framework import test
from rest_framework.test import APIClient

from accounts.models import Account


class APITestCase(test.APITestCase):
    def setUp(self):
        super(APITestCase, self).setUp()

    def assertContentEquals(self, response, dict):
        raise Exception("What?")

    def assertTotalCountEquals(self, response, count):
        try:
            self.assertEqual(response.data.get('meta', {}).get('count'), count)
        except AttributeError:
            raise Exception("Return type was unexpected:\n\n%s" % response.data)


class DefaultSetup(test.APITestCase):
    def setUp(self):
        super(DefaultSetup, self).setUp()

        self.account = self.create_user(
            username='abraham',
            email='abraham@washington.gov',
            password='P@ssw0rd!')
        self.client = test.APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.account.auth_token.key)

    def create_user(self,
                    username='george',
                    email='george@washington.gov',
                    password='testtest',
                    **kwargs):
        account = Account.objects.create(
            username=username,
            email=email,
            password=password,
            **kwargs,
        )
        account.set_password(password)
        account.save()
        setattr(account, 'clear_password', password)
        return account

    def create_client(self, account=None):
        client = APIClient()
        if account:
            client.credentials(HTTP_AUTHORIZATION='Token ' + account.auth_token.key)
        return client
