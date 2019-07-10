from django.urls import reverse
from rest_framework import status

from helpers.test import DefaultSetup


class BillsTest(DefaultSetup):

    def setUp(self):
        super(BillsTest, self).setUp()

    def test_get_bills(self):
        response = self.client.get(reverse('bill-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
