from django.db import models

class Subject(models.Model):
    class SubjectChoices(models.TextChoices):
        IMAGE = ("image", "image")
        VIDEO = ("video", "video")

    subject_url = models.FileField()
    type = models.CharField(
        max_length=10,
        choices=SubjectChoices.choices,
    )

    def __str__(self):
        return self.type
