from rest_framework import serializers
from .models import Post
from contents.serializers import ContentSerializer
from users.serializers import UsersSerializer

class PostSerializer(serializers.ModelSerializer):
    contents = ContentSerializer(
        read_only=True,
        many=True,
    )

    users = UsersSerializer(
        read_only=True,
    )

    class Meta:
        model = Post
        fields = "__all__"
        depth = 1
