from .models import LapizuaPocket
from celery import shared_task
from django.utils import timezone
import datetime

@shared_task(name='delete_old_lapizua_pockets')
def delete_old_lapizua_pockets():
    d = timezone.now() - datetime.timedelta(hours=24)
    print(d)
    pockets = LapizuaPocket.objects.filter(created_at__lt=d)
    pockets.delete()