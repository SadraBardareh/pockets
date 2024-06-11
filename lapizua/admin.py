from django.contrib import admin
from .models import LapizuaPocket

@admin.register(LapizuaPocket)
class LapizuaPocketAdmin(admin.ModelAdmin):
    search_fields = ['name', 'id']
    list_display = ['id', 'name', 'created_at']
    list_per_page = 10