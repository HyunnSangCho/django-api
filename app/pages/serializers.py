from rest_framework import serializers
from .models import Page
from posts.serializers import PostSerializer

class PageSerializer(serializers.ModelSerializer):
    posts = PostSerializer(
        read_only=True,
        many=True,
    )

    class Meta:
        model = Page
        fields = (
            "posts",
            "count"
        )