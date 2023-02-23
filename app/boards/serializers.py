from rest_framework import serializers
from .models import Board
from subjects.serializers import SubjectSerializer
from people.serializers import PeopleSerializer

class BoardSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer(
        read_only=True,
        many=True,
    )

    people = PeopleSerializer(
        read_only=True,
    )

    class Meta:
        model = Board
        fields = "__all__"
        depth = 1
