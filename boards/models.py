from django.db import models

class Board(models.Model):
    subjects = models.ManyToManyField("subjects.Subject", related_name="boards")
    description = models.CharField(max_length=350)
    people = models.ForeignKey(
        "people.People",
        on_delete=models.CASCADE,
        related_name="boards"
    )
    good_counts = models.PositiveIntegerField()

    def __str__(self):
        return self.people.name