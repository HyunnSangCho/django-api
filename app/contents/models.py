from django.db import models

class Content(models.Model):
    class ContentChoices(models.TextChoices):
        IMAGE = ("image", "image")
        VIDEO = ("video", "video")

    content_url = models.FileField()
    type = models.CharField(
        max_length=10,
        choices=ContentChoices.choices,
    )

    def __str__(self):
        return self.content_url.name
