from django.contrib.auth import get_user_model
from django.db import models


class Favorite(models.Model):
    username = models.ManyToManyField("accounts.CustomUser", blank=True)
    name = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)