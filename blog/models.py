from django.contrib.auth import get_user_model
from django.db import models


class Blog(models.Model):
    username = models.ForeignKey(get_user_model(), on_delete=models.CASCADE())
    heading = models.CharField(max_length=255)
    blog_entry = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.heading
