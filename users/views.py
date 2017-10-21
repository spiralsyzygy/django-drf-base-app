# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth import views as auth_views
from django.shortcuts import render
from django.views.generic import CreateView
from .forms import SignUpForm
from django.urls import reverse

class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'signup.html'

    def get_success_url(self):
        return settings.SIGNUP_REDIRECT_URL

class LoginView(auth_views.LoginView):
    template_name = 'login.html'

class LogoutView(auth_views.LogoutView):
    pass

class PasswordChange(auth_views.PasswordChangeView):
    template_name = 'password_change.html'

class PasswordChangeDone(auth_views.PasswordChangeDoneView):
    template_name = 'password_change_done.html'
