from django.contrib.auth import get_user_model
from django.db import models


ORIGIN_CHOICES = (
    "american",
    "lao",
    "thai",
    "vietnamese",
    "korean",
    "chinese",
    "japanese",
    "other"
)


# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=255)
    origin = models.CharField(max_length=32, choices=ORIGIN_CHOICES, default="other")
    username = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    ingredients = models.ManyToManyField("ingredients.Ingredient")

