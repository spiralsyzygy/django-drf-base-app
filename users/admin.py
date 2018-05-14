# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class MyUserAdmin(UserAdmin):
    readonly_fields = ('last_login', 'date_joined')


admin.site.register(User, MyUserAdmin)
