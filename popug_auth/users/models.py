from django.db import models
from .managers import CustomUserManager

from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=30)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email