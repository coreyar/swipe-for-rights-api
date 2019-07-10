from django.urls import reverse
from rest_framework import status

from helpers.test import DefaultSetup


class AccountTest(DefaultSetup):

    def setUp(self):
        super(AccountTest, self).setUp()

    def login(self, username, password, client=None):
        if client:
            return client.post(reverse('account-login'), {'username': username, 'password': password})
        return self.client.post(reverse('account-login'), {'username': username, 'password': password})

    def test_login_with_username(self):
        account = self.create_user(username='logintest', password='t35T*test')
        client = self.create_client(account)
        response = self.login(account.username, account.clear_password, client=client)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.data.get('data', False)
        self.assertNotEqual(data, False)
        self.assertEqual(data.get('id', False), str(account.id), data)
        self.assertEqual(data.get('username', False), account.username, data)

    def test_login_fails_for_incorrect_password(self):
        account = self.create_user(username='incorrectpassword')

        response = self.login(account.username, 'wrong')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_login_fails_for_incorrect_username(self):
        account = self.create_user(username='incorrectusername', password='t35T*test')

        response = self.login('george@washington.gov', account.clear_password)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_me(self):
        response = self.client.get(reverse('account-me'))
        self.assertEqual(response.data.get('data').get('id'), str(self.account.id))

    def test_update_me(self):
        request_data = {
            'username': 'abraham',
        }

        response = self.client.post(reverse('account-me'), request_data)

        def check_field(name):
            self.assertEqual(response.data.get('data').get(name), request_data.get(name))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for field in request_data:
            check_field(field)
