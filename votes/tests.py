from django.urls import reverse
from rest_framework import status

from helpers.test import DefaultSetup


class VotesTest(DefaultSetup):

    def setUp(self):
        super(VotesTest, self).setUp()

    def test_submit_vote(self):
        response = self.client.put(reverse('vote-detail', kwargs={'pk': '123'}), {'supports': True})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
