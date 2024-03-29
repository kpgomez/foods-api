from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    username = models.CharField(max_length=128)
    email = models.CharField(max_length=128)

    def __str__(self):
        return self.username
