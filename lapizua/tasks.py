from .models import LapizuaPocket
from celery import shared_task
from django.utils import timezone
import datetime

@shared_task
def delete_old_lapizua_pockets():
    d = timezone.now() - datetime.timedelta(hours=24)
    pockets = LapizuaPocket.objects.filter(created_at__lt=d)
    pockets.delete()