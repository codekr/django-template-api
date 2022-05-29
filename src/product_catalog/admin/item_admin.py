from django.contrib import admin
from django.db import models
from django.forms import Textarea, TextInput
from import_export.admin import ImportExportModelAdmin

from ..models import Item
from ..resources import ItemResource


@admin.register(Item)
class ItemAdmin(ImportExportModelAdmin):
    resource_class = ItemResource
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '60'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 2, 'cols': 100, 'style': 'resize:none;'})},
    }
    fieldsets = (
        (None, {
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
    ordering = ('-updated_at',)
    list_per_page = 120
