from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

client = APIClient()

url = '/weather/'


class WeatherTestCase(TestCase):

    def test_get_weather(self):
        response = client.get(
            url,
            {'city': 'dhaka'},
            format='json',
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_wrong_city_name(self):
        response = client.get(
            url,
            {'city': 'chemondis'},
            format='json',
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_wrong_city_name(self):
        response = client.get(
            url,
            {'city': 'chemondis'},
            format='json',
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
