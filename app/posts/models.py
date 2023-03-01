from django.db import models

class Post(models.Model):
    contents = models.ManyToManyField("contents.Content", related_name="posts")
    description = models.TextField()
    users = models.ForeignKey(
        "users.Users",
        on_delete=models.CASCADE,
        related_name="posts"
    )
    like_count = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.users.display_name}'s posts"