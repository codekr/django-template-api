from django.contrib import admin
from django.db import models
from django.forms import Textarea, TextInput
from import_export.admin import ImportExportModelAdmin

from ..models import Category


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '60'})},
        models.PositiveIntegerField: {'widget': TextInput(attrs={'size': '25'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 2, 'cols': 100, 'style': 'resize:none;'})},
    }
    fieldsets = (
        ("Category", {
            'fields': (
                'name',
                'description',
                'display_order',
                'background_hex_code',
                'is_approved'
            ),
        }),
    )
    list_display = (
        'category_id', 'display_order', 'image', 'name', 'sub_category_count', 'background_hex_code', 'is_approved',
        'created_at', 'updated_at'
    )
    list_select_related = ('image',)
    list_display_links = ('category_id', 'image',)
    list_filter = ('created_at', 'updated_at')
    search_fields = ('category_id', 'name',)
    autocomplete_fields = ('image',)
    ordering = ('-updated_at',)

    def get_queryset(self, request):
        qs = super(CategoryAdmin, self).get_queryset(request)
        return qs.prefetch_related('sub_categories')

    def sub_category_count(self, obj):
        return obj.sub_categories.all().count()
