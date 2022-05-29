from django.contrib import admin
from django.db import models
from django.forms import Textarea
from import_export.admin import ImportExportModelAdmin

from ..models import Item


@admin.register(Item)
class ItemAdmin(ImportExportModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 2, 'cols': 100, 'style': 'resize:none;'})},
    }
    fieldsets = (
        ("Item Form", {
            'fields': (
                'item_name',
                'item_alternate_name',
                'is_approved'
            ),
        }),
    )
    list_display = (
        'item_id', 'item_name', 'item_alternate_name',
        'is_approved', 'created_at', 'updated_at'
    )
    list_filter = ('created_at', 'updated_at')
    search_fields = ('item_id', 'item_name', 'item_alternate_name',)
    ordering = ('updated_at',)
