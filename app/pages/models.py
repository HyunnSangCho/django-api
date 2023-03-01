from django.db import models

class Page(models.Model):
    count = models.PositiveIntegerField(blank=True, null=True, default=5)
    posts = models.ManyToManyField("posts.Post")

