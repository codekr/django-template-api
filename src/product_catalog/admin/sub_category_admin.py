from django.contrib import admin
from django.db import models
from django.forms import Textarea, TextInput
from import_export.admin import ImportExportModelAdmin

from ..models import SubCategory, CategorySubCategory


class CategoriesInline(admin.TabularInline):
    model = CategorySubCategory
    autocomplete_fields = ['category']
    verbose_name = "Categories"


@admin.register(SubCategory)
class SubCategoryAdmin(ImportExportModelAdmin):
    inlines = [CategoriesInline]
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '60'})},
        models.PositiveIntegerField: {'widget': TextInput(attrs={'size': '25'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 3, 'cols': 100, 'style': 'resize:none;'})},
    }
    fieldsets = (
        ("Sub Category Form", {
            'fields': (
                'name',
                'description',
                'display_order',
                'background_hex_code',
            ),
        }),
        ("Effective", {
            'fields': (
                ('effective_start_date', 'effective_end_date',)
            ),
        }),
        ("Other Information", {
            'fields': (
                ('is_approved', 'is_tax_applicable',)
            ),
        }),
    )
    list_display = (
        'sub_category_id', 'display_order', 'image', 'name',
        'background_hex_code', 'is_approved', 'is_tax_applicable',
        'effective_start_date', 'effective_end_date', 'created_at', 'updated_at'
    )
    list_select_related = ('image',)
    list_display_links = ('sub_category_id', 'image',)
    list_filter = ('created_at', 'updated_at', 'effective_start_date', 'effective_end_date', 'is_tax_applicable',)
    search_fields = ('sub_category_id', 'name',)
    autocomplete_fields = ('image',)
    ordering = ('-updated_at',)
