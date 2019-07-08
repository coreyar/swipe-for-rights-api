import logging

from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from djongo.models.fields import ArrayModelField
from .managers import AccountManager
from votes.models import Vote
from votes.forms import VoteForm
logger = logging.getLogger('{{cookiecutter.app_name}}')


class Account(AbstractBaseUser, PermissionsMixin):
    objects = AccountManager()

    class Meta:
        ordering = ('-id',)

    USERNAME_FIELD = settings.ACCOUNT_NATURAL_KEY
    REQUIRED_FIELDS = ['email']
    MINIUM_USERNAME_LENGTH = 3

    username: str = models.CharField('username', max_length=32, unique=True)
    email = models.EmailField('email address', unique=True, default=None, null=True, blank=True)
    password = models.CharField(_('password'), max_length=128, default=None, null=True, blank=True)
    first_name: str = models.CharField('First Name', max_length=32, default=None, null=True, blank=True)
    last_name: str = models.CharField('Last Name', max_length=32, default=None, null=True, blank=True)

    is_staff = models.BooleanField('staff status', default=False,
                                   help_text=_('Designates whether the user can log into this admin site.'))
    is_active = models.BooleanField('active', default=True,
                                    help_text=_('Designates whether this user should be treated as '
                                                'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    votes = ArrayModelField(
        model_container=Vote,
        model_form_class=VoteForm,
        blank=True,
        default=[],
    )

    def __str__(self) -> str:
        return '{} {}'.format(self.first_name, self.last_name)

    def get_full_name(self) -> str:
        return '{} {}'.format(self.first_name, self.last_name)
