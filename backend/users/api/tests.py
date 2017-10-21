# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from requests_jwt import JWTAuth

User = get_user_model()

from rest_framework import status
from rest_framework_jwt.settings import api_settings


class APIJWTClient(APIClient):
    def login(self, credentials):
        """
        Returns True if login is possible; False if the provided credentials
        are incorrect, or the user is inactive.
        """

        response = self.post('/api/token-auth/', credentials, format='json')
        if response.status_code == status.HTTP_200_OK:
            self.credentials(
                HTTP_AUTHORIZATION="{0} {1}".format(api_settings.JWT_AUTH_HEADER_PREFIX, response.data['token']))

            return True
        else:
            return False


class UserAPITestCase(APITestCase):
    client_class = APIJWTClient

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            'foobar', email='foo@bar.com', password='password'
        )
        cls.super_user = User.objects.create_superuser(
            'administrator', email='baz@buzz.com', password='secret'
        )

    def test_00signup(self):
        client = APIClient()
        print "Testing Signup"
        response = client.post('/api/signup/',
                               {
                                'username': 'user1',
                                'email': 'email@email.com',
                                'password': 'password',
                               },
                                format='json'
        )
        # if it's successful it return 201 Created
        print "Checking response is 201"
        self.assertEqual(response.status_code, 201)
        print "Passed"

        print "Querying user by email"
        user = User.objects.get(email="email@email.com")
        self.assertEqual(user.username, "user1")
        print "Passed"

        response = client.post('/api/signup/',
                               {
                                'username': 'user1',
                                'email': 'email@email.com',
                                'password': 'password',
                               },
                                format='json'
        )

    def test_01login(self):
        print "Testing Login with bad password"
        response = self.client.post('/api/token-auth/', {
            "username": "foobar",
            "password": "bad-pass"
        }, format='json')
        self.assertEqual(response.status_code, 400)
        print "Passed"

        print "Testing Login"
        response = self.client.post('/api/token-auth/', {
            "username": "foobar",
            "password": "password"
        }, format='json')

        print "Checking for token"
        self.assertIn('token', response.data)
        self.assertIsNot(response.data['token'], None)
        print "Passed!"


    def test_02change_password(self):
        print "Testing password change"
        self.assertTrue(self.client.login({
            "username": "foobar",
            "password": "password"
        }))
        response = self.client.patch(reverse('api-password-change', kwargs={'pk': 1}),{"password": "password1"})
        self.assertEqual(response.status_code, 204)
        print "Passed!"

        print "Testing Login with new password"
        response = self.client.post('/api/token-auth/', {
            "username": "foobar",
            "password": "password1"
        }, format='json')

        print "Checking for token"
        self.assertIn('token', response.data)
        self.assertIsNot(response.data['token'], None)
        print "Passed!"
