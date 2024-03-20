from unittest import TestCase
from rest_framework.test import APIClient


class TestSmth(TestCase):
    def test_one(self):
        client = APIClient()
        url = '/api/v1/products/'
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
