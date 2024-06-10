from django.db import models
from uuid import uuid4

class LapizuaPocket(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=255)
    text = models.TextField(max_length=1023)