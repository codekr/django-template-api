from django.db import models
from django.utils.translation import gettext_lazy as _


class NotificationOperationTypeChoice(models.TextChoices):
    SMS = 'Sms', _('SMS'),
    EMAIL = 'Email', _('EMAIL'),
    EMAIL_SMS = 'Email_Sms', _('EMAIL/SMS'),


class NotificationOperationAreaChoice(models.TextChoices):
    Orders = 'Orders', _('Orders'),
    Refunds = 'Refunds', _('Refunds'),
    Catalog = 'Catalog', _('Catalog')


class NotificationOperationTriggerActionChoice(models.TextChoices):
    NEW_ORDER = 'NEW_ORDER', _('When New Order Placed'),
    DAILY_ORDER = 'DAILY_ORDER', _('Daily Order Value'),


class NotificationOperation(models.Model):
    notification_operation_id = models.AutoField(primary_key=True)
    area = models.CharField(
        max_length=120,
        choices=NotificationOperationAreaChoice.choices,
        db_index=True,
        verbose_name="Area",
        help_text=""
    )
    trigger_action = models.CharField(
        max_length=255,
        choices=NotificationOperationTriggerActionChoice.choices,
        verbose_name="Trigger On",
        db_index=True,
        help_text=""
    )
    type = models.CharField(
        max_length=255,
        choices=NotificationOperationTypeChoice.choices,
        db_index=True,
        verbose_name="Notification Channel",
        help_text=""
    )
    sms_content = models.TextField(
        max_length=255,
        null=True, blank=True,
        verbose_name="SMS Message Content",
        help_text=""
    )
    email_content = models.TextField(
        null=True, blank=True,
        verbose_name="Email Message Content",
        help_text=""
    )
    frequency = models.PositiveSmallIntegerField(
        null=True, blank=True,
        default=1,
        db_index=True,
        verbose_name="Notification Frequency",
        help_text=""
    )
    time = models.TimeField(
        null=True, blank=True,
        db_index=True,
        verbose_name="At Time",
        help_text=""
    )
    email_recipient = models.TextField(
        max_length=1000,
        null=True,
        blank=True,
        verbose_name="Recipient's Email Addresses",
        help_text="Comma separated email address, e.g dinesh@radiansys.com, dheeraj@radiansys.com"
    )
    sms_recipient = models.TextField(
        max_length=1000,
        null=True,
        blank=True,
        verbose_name="Recipient's Phone Numbers",
        help_text="Comma separated phone number including country code, e.g +1543678909, +9187676545656"
    )
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'notification_operation_mst'
        verbose_name = 'Notification Operation'

    def __str__(self):
        return f"Notification Operation: {self.notification_operation_id}"
