
from django.db import models


class Post(models.Model):
    """this model helps to store post model data"""
    title = models.CharField(max_length=50, blank=True, default="")
    descriptions = models.TextField()
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
