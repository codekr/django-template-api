from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea
from import_export.admin import ImportExportModelAdmin

from ..models import NotificationOperation


@admin.register(NotificationOperation)
class NotificationOperationAdmin(ImportExportModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '60'})},
        models.PositiveIntegerField: {'widget': TextInput(attrs={'size': '25'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 100, 'style': 'resize:none;'})},
    }
    fieldsets = (
        ("Notification Area", {
            'fields': (
                'area',
            ),
        }),
        ("Periodic Information", {
            'fields': (
                'trigger_action', 'type',
                'frequency', 'time'
            ),
        }),
        ("Message Content Information", {
            'fields': (
                'sms_content', 'email_content',
            ),
        }),
        ("Recipients Information", {
            'fields': (
                'email_recipient', 'sms_recipient',
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
