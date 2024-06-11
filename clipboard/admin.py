from django.contrib import admin
from .models import Clipboard, ClipboardItem

class ClipboardItemInline(admin.StackedInline):
    autocomplete_fields = ['clipboard']
    model = ClipboardItem
    extra = 0
    min_num = 1
    max_num = 20
@admin.register(Clipboard)
class ClipboardAdmin(admin.ModelAdmin):
    autocomplete_fields = ['user']
    search_fields = ['name', 'id']
    inlines = [ClipboardItemInline]
    list_display = ['name', 'user', 'id']
    list_per_page = 10

