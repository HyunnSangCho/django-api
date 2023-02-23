from rest_framework import serializers
from .models import Clone
from boards.serializers import BoardSerializer

class CloneSerializer(serializers.ModelSerializer):
    boards = BoardSerializer(
        read_only=True,
        many=True,
    )

    class Meta:
        model = Clone
        fields = (
            "boards",
        )