from django.test import TestCase
from django.shortcuts import redirect


class HomePageTest(TestCase):

    def test_home_page(self):
        client = self.client.get('/')
        self.assertEqual(client.status_code, 200)