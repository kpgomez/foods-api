from django.db import models


class Inventory(models.Model):
    ingredients = models.ForeignKey()
