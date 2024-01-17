# inventory/models.py
from django.db import models
from multiselectfield import MultiSelectField


CATEGORY_CHOICES = (
    "vegetable",
    "fruit",
    "dairy",
    "protein",
    "fresh herb",
    "seasoning",
    "sauce",
    "liquid",
    "other"
)

COST_RATING_CHOICES = (
    "low",
    "medium",
    "high"
)

PURCHASE_OPTIONS = (
    "locally",
    "big_city",
    "online"
)


# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=32)
    recipes = models.ManyToManyField("recipes.Recipe", blank=True)
    category = models.CharField(max_length=32, choices=CATEGORY_CHOICES, default="other")
    cost_rating = models.CharField(max_length=16, choices=COST_RATING_CHOICES, default="low")
    current_inventory = models.PositiveSmallIntegerField(default=0)
    purchase_options = models.MultiSelectField(choices=PURCHASE_OPTIONS)
