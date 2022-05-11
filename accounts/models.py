from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.db import models


class Account(AbstractUser):
    email = models.EmailField(
        _('email address'), unique=True,
        error_messages = {
            'required': _('Must provide a valid email address.'),
            'invalid': _('Must provide a valid email address.'),
        },
    )
    first_name = models.CharField(
        _('first name'), max_length=30,
        error_messages = {
            'required': _('Must provide a first name.'),
            'max_length': _('First name can be at most 150 characters.'),
        },
    )
    last_name = models.CharField(
        _('last name'), max_length=30,
        error_messages = {
            'required': _('Must provide a last name.'),
            'max_length': _('Last name can be at most 150 characters.'),
        }
    )
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
