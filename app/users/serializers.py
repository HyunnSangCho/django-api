from rest_framework import serializers
from .models import Users

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = (
            "display_name",
            "follow_count",
            "profile_thumbnail_url"
        )
