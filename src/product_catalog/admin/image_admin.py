from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea
from import_export.admin import ImportExportModelAdmin

from ..models import Image


@admin.register(Image)
class ImageAdmin(ImportExportModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '60'})},
        models.PositiveIntegerField: {'widget': TextInput(attrs={'size': '25'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 2, 'cols': 100, 'style': 'resize:none;'})},
    }
    fieldsets = (
        ("Image Form", {
            'fields': (
                'filename',
                'alt_text'
            ),
        }),
    )
    list_display = (
        'image_id', 'filename', 'alt_text',
        'storage_id', 'type', 'created_at', 'updated_at'
    )
    list_filter = ('created_at', 'updated_at')
    search_fields = ('image_id', 'filename', 'alt_text',)
    ordering = ('-updated_at',)
