from functools import total_ordering
from rest_framework import serializers
from backendApp.models import PlayerClass

class PlayerClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerClass
        fields = ('id', 'name', 'password', 'wins')