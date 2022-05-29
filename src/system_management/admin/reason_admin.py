from django.contrib import admin
from django.db import models
from django.forms import Textarea
from import_export.admin import ImportExportModelAdmin

from ..models import Reason


@admin.register(Reason)
class ReasonAdmin(ImportExportModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 3, 'cols': 100, 'style': 'resize:none;'})},
    }
    fieldsets = (
        ("Forms", {
            'fields': (
                'reason_type',
                'reason_label'
            ),
        }),
    )

    list_display = (
        'reason_id', 'reason_type', 'reason_label', 'created_at', 'updated_at',
    )
    list_filter = ('reason_type',)
    search_fields = ('reason_id', 'reason_type', 'reason_label')
    ordering = ('-updated_at',)
