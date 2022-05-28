from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models

from djmoney.models.fields import MoneyField
from src.system_management.models import NotificationOperation


@admin.register(NotificationOperation)
class NotificationOperationAdmin(ImportExportModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '60'})},
        models.PositiveIntegerField: {'widget': TextInput(attrs={'size': '25'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 100, 'style': 'resize:none;'})},
    }
    fieldsets = (
        ("Forms", {
            'fields': (
                ('area', 'trigger_action', 'type',),
                'frequency', 'time',
                ('sms_content', 'email_content',),
                ('email_recipient', 'sms_recipient',),
                'is_active'
            ),
        }),
    )

    list_display = (
        'notification_operation_id', 'area', 'trigger_action', 'type', 'frequency', 'email_recipient', 'sms_recipient',
        'is_active', 'created_at',
        'updated_at',
    )
    list_filter = ('area', 'trigger_action', 'type')
    search_fields = ('notification_operation_id', 'area', 'trigger_action', 'type')
    ordering = ('updated_at',)
