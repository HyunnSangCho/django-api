from django.db import models

class Users(models.Model):
    display_name = models.CharField(max_length=100)
    follow_count = models.PositiveIntegerField()
    profile_thumbnail_url = models.ImageField()

    def __str__(self):
        return self.display_name