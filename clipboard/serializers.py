from rest_framework import serializers
from .models import Clipboard, ClipboardItem
from uuid import uuid4

class ClipboardSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = Clipboard
        fields = ['id', 'name', 'user_id']
    def create(self, validated_data):
        user_id = self.context['user_id']
        return Clipboard.objects.create(user_id=user_id, **validated_data)
    
class ClipboardItemSerializer(serializers.ModelSerializer):
    clipboard_id = serializers.UUIDField(read_only=True)
    class Meta:
        model = ClipboardItem
        fields = ['id', 'name', 'text', 'clipboard_id']
    def create(self, validated_data):
        clipboard_id = self.context['clipboard_id']
        return ClipboardItem.objects.create(clipboard_id=clipboard_id, **validated_data)