from django.contrib.auth.models import AbstractUser
from django.db import models

from customer.managers import CustomUserManager


class CustomUser(AbstractUser):
    email = models.EmailField("Email",
                              null=True,
                              unique=True)
    first_name = models.CharField("First name",
                                  max_length=150,
                                  null=True,
                                  blank=True)
    last_name = models.CharField("Last name",
                                 max_length=150,
                                 null=True,
                                 blank=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    username = models.CharField("username",
                                max_length=150,
                                unique=True,
                                null=True)

    def __str__(self):
        return self.username

    objects = CustomUserManager()
