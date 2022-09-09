from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from .models import Account

# Create your tests here.
class URLTests(APITestCase):
    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_authorization(self):
        self.client = APIClient()
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, 401)

