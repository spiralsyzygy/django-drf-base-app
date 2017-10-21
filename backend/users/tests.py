# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase, Client
# from django.test.client import encode_multipart, RequestFactory
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth import login, logout
from django.urls import reverse

User = get_user_model()

# settings
# SIGNUP_REDIRECT_URL = '/home/'
# LOGIN_URL = '/login/'
# LOGIN_REDIRECT_URL = '/home/'
# LOGOUT_URL = '/logout/'
# LOGOUT_REDIRECT_URL = '/login/'

class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            'foobar', email='foo@bar.com', password='password'
        )
        cls.super_user = User.objects.create_superuser(
            'administrator', email='baz@buzz.com', password='secret'
        )

    def test_users_created(self):
        assert(self.user.email == 'foo@bar.com')
        assert(self.user.username == 'foobar')
        assert(self.user.is_staff == False)
        assert(self.user.is_superuser == False)

    def test_super_user_created(self):
        assert(self.super_user.email == 'baz@buzz.com')
        assert(self.super_user.username == 'administrator')
        assert(self.super_user.is_staff == True)
        assert(self.super_user.is_superuser == True)

    def test_signup(self):
        # This must exercise the entire model, form, view, url path
        response = self.client.post(reverse("signup"), {
            "username": "user1",
            "email": "email@email.com",
            "password1": "password",
            "password2": "password"}
        )
        user = User.objects.get(email="email@email.com")
        self.assertEqual(user.username, "user1")
        # if it's successful it redirects.
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, settings.SIGNUP_REDIRECT_URL)

    def test_login(self):
        response = self.client.post(settings.LOGIN_URL, {
            "username": "foobar",
            "password": "password"
        })
        # if it's successful it redirects.
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, settings.LOGIN_REDIRECT_URL)

    def test_logout(self):
        response = self.client.post(settings.LOGOUT_URL)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, settings.LOGOUT_REDIRECT_URL)

    def test_password_change(self):
        # login
        response = self.client.post(settings.LOGIN_URL, {
                    "username": "foobar",
                    "password": "password"
        })
        self.assertEqual(response.status_code, 302)
        # change password
        response = self.client.post(reverse('password_change'), {
                    "old_password": "password",
                    "new_password1": "password1",
                    "new_password2": "password1"
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('password_change_done'))
        # logout
        response = self.client.post(settings.LOGOUT_URL)
        self.assertEqual(response.status_code, 302)
        response = self.client.post(settings.LOGIN_URL, {
                    "username": "foobar",
                    "password": "password1"
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, settings.LOGIN_REDIRECT_URL)
