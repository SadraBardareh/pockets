from .models import LapizuaPocket
from rest_framework import serializers

class LapizuaPocketSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = LapizuaPocket
        fields = ['id', 'name', 'text']
