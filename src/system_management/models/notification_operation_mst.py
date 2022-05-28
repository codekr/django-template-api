from django.db import models
from django.utils.translation import gettext_lazy as _


class NotificationOperationTypeChoice(models.TextChoices):
    Email = 'Email', _('Email'),
    Text = 'Text', _('Text'),


class NotificationOperationTriggerActionChoice(models.TextChoices):
    Email = 'Email', _('Email'),
    Text = 'Text', _('Text'),


class NotificationOperation(models.Model):
    notification_operation_id = models.AutoField(primary_key=True)
    area = models.CharField(max_length=120, null=False, blank=False, db_index=True)
    trigger_action = models.CharField(
        max_length=255, null=False, blank=False, db_index=True,
        choices=NotificationOperationTriggerActionChoice.choices
    )
    type = models.CharField(
        max_length=255, null=False, blank=False, db_index=True,
        choices=NotificationOperationTypeChoice.choices)

    email_content = models.TextField(null=True, blank=True)
    text_content = models.TextField(max_length=255, null=True, blank=True)
    frequency = models.PositiveSmallIntegerField(null=True, blank=True, db_index=True, default=1)
    time = models.TimeField(null=True, blank=True, db_index=True)
    email_recipient = models.TextField(max_length=255, null=False, blank=False, db_index=True)
    text_recipient = models.TextField(max_length=255, null=False, blank=False, db_index=True)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'notification_operation_mst'
        verbose_name = 'Internal Notification Operation'

    def __str__(self):
        return f"Notification Operation: {self.notification_id}"
