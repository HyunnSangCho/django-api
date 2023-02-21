from django.db import models

class People(models.Model):
    name = models.CharField(max_length=100)
    follower = models.PositiveIntegerField()
    profile_url = models.URLField()

    def __str__(self):
        return self.name