from django.contrib.auth.models import UserManager


class UserManager(UserManager):
    def create_user(self, username, email=None, password=None, **kwargs):
        # add custom stuff here
        account = super(UserManager, self).create_user(
            username, email=email, password=password, **kwargs
        )
        return account

    def create_superuser(self, username, email=None, password=None, **kwargs):
        account = super(UserManager, self).create_superuser(
            username, email=email, password=password, **kwargs
        )
        return account
