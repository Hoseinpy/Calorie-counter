from rest_framework.test import APITestCase
from django.urls import reverse
from home.models import Food


class ApiTest(APITestCase):

    def test_food_list(self):
        response = self.client.get(reverse('food-list-api'))
        self.assertEqual(response.status_code, 200)

    def test_user_food_list(self):
        response = self.client.get(reverse('user-food-list-api'))
        self.assertEqual(response.status_code, 200)