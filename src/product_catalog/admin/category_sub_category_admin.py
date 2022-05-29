from django.contrib import admin
from django.db import models
from django.forms import Textarea, TextInput
from import_export.admin import ImportExportModelAdmin

from ..models import CategorySubCategory


@admin.register(CategorySubCategory)
class CategorySubCategoryAdmin(ImportExportModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '60'})},
        models.PositiveIntegerField: {'widget': TextInput(attrs={'size': '25'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 2, 'cols': 100, 'style': 'resize:none;'})},
    }
    fieldsets = (
        ("Form", {
            'fields': (
                'category',
                'sub_category',
            ),
        }),
    )
    list_display = (
        'category_sub_category_id', 'category', 'sub_category', 'created_at', 'updated_at'
    )
    list_display_links = ('category', 'sub_category',)
    list_filter = ('updated_at',)
    list_select_related = ('category', 'sub_category',)
    autocomplete_fields = ('category', 'sub_category',)
    search_fields = (
        'category_sub_category_id', 'category__name', 'sub_category__name')
    ordering = ('-updated_at',)
