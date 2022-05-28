from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models

from djmoney.models.fields import MoneyField
from src.system_management.models import IssueReason


@admin.register(IssueReason)
class IssueReasonAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '40'})},
        models.PositiveIntegerField: {'widget': TextInput(attrs={'size': '25'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 100})},
    }
    fieldsets = (
        (None, {
            'fields': (
                'reason_type',
                'reason_label'
            ),
        }),
    )

    list_display = (
        'issue_reason_id', 'reason_type', 'reason_label', 'created_at', 'updated_at',
    )
    list_filter = ('reason_type',)
    search_fields = ('issue_reason_id', 'reason_type', 'reason_label')
    ordering = ('updated_at',)
