from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea
from import_export.admin import ImportExportModelAdmin

from ..models import Brand
from ..resources import BrandResource


@admin.register(Brand)
class BrandAdmin(ImportExportModelAdmin):
    resource_class = BrandResource
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '60'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 2, 'cols': 100, 'style': 'resize:none;'})},
    }
    fieldsets = (
        ("Brand Form", {
            'fields': (
                'brand_name',
                ('is_exclusive', 'is_recognised_brand', 'is_approved')
            ),
        }),
    )
    list_display = (
        'brand_id', 'brand_name',
        'is_exclusive', 'is_recognised_brand', 'is_approved',
        'created_at', 'updated_at'
    )
    list_select_related = ('image',)
    list_filter = ('created_at', 'updated_at', 'brand_name')
    search_fields = ('brand_id', 'brand_name',)
    autocomplete_fields = ('image',)
    ordering = ('updated_at',)
