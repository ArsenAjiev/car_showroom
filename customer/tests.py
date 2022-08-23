from django.test import TestCase
from rest_framework.test import APIClient, APITestCase
from django.urls import reverse
from customer.models import Customer


# Test example
class TestStringMethods(TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')


# User Registration
class RegistrationTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.login_url = reverse('customer-list')

    def test_user_registration(self):
        """
        User registration
        """
        credentials = {
            'username': 'user1',
            'password': 'passw',
            'email': 'qw@asd.py',
            'password2': 'passw',
        }
        response = self.client.post(self.login_url, credentials)
        self.assertEqual(response.status_code, 201)


# User Authentication
class AuthenticatorTestCase(APITestCase):
    def setUp(self):
        self.user = Customer.objects.create_user('user1', 'user@user.com', 'passw')
        self.client = APIClient()
        self.login_url = reverse('rest_framework:login')

    def test_login_return(self):
        """
        The login view return
        """
        credentials = {
            'username': 'user1',
            'password': 'passw',
        }
        response = self.client.post(self.login_url, credentials)
        self.assertEqual(response.status_code, 302)
