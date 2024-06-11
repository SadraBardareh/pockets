from django.db import models
from django.conf import settings
from uuid import uuid4

class Clipboard(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=255, unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name

class ClipboardItem(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField(max_length=1023)
    clipboard = models.ForeignKey(Clipboard, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name