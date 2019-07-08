from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth.models import BaseUserManager
from django.utils import timezone

NATURAL_KEY = getattr(settings, 'ACCOUNT_NATURAL_KEY', 'username')


class AccountManager(BaseUserManager):

    def get_by_natural_key(self, val):
        lookup = {NATURAL_KEY: val}
        return self.get(**lookup)

    def create_user(self, username=None, password=None, **extra_fields):
        """
        Creates and saves a User with the given username and password.
        """
        now = timezone.now()
        username = AccountManager.normalize_username(username)
        user = self.model(username=username, is_staff=False, is_active=True, is_superuser=False,
                          last_login=now, date_joined=now, **extra_fields)
        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.username = username
        user.admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
