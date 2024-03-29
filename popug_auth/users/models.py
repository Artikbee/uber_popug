import uuid

from django.db import models
from .managers import CustomUserManager

from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
)

ROLE_CHOICES = {
    'admin': 'admin',
    'popug': 'popug',
    'top manager': 'top manager',

}


class CustomUser(AbstractBaseUser, PermissionsMixin):

    public_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True)

    name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=30, choices=ROLE_CHOICES)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
