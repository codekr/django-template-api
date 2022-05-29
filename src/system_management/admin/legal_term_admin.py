from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea
from import_export.admin import ImportExportModelAdmin

from ..models import LegalTerm


@admin.register(LegalTerm)
class LegalTermAdmin(ImportExportModelAdmin):
    required_css_class = 'required'
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '80'})},
        models.PositiveIntegerField: {'widget': TextInput(attrs={'size': '25'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 100, 'style': 'resize:none;'})},
    }
    fieldsets = (
        ("Legal Terms Form", {
            'fields': (
                'term_type', 'legal_file_name',
                'effective_from', 'version'
            ),
        }),
    )

    list_display = (
        'legal_terms_id', 'term_type', 'legal_file_name', 'effective_from', 'version', 'created_at',
        'updated_at',
    )
    list_filter = ('updated_at', 'effective_from')
    search_fields = ('legal_terms_id', 'term_type', 'effective_from', 'version')
    ordering = ('-updated_at',)
