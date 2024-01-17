from django.contrib.auth import get_user_model
from django.db import models


class GroceryList(models.Model):
    username = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    ingredients = models.ManyToManyField("ingredients.Ingredient", blank=True)

    def __str__(self):
        return f"{self.username}'s Grocery List"
