from rest_framework import serializers
from .models import Content

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = (
            "content_url",
            "type",
        )
        