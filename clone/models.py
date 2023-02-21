from django.db import models

class Clone(models.Model):
    count = models.PositiveIntegerField(blank=True, null=True)
    page = models.PositiveIntegerField(blank=True, null=True)
    boards = models.ManyToManyField("boards.Board", related_name="clone")

