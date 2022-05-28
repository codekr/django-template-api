from django.db import models
from django.utils.translation import gettext_lazy as _


class IssueReasonTypeChoice(models.TextChoices):
    Delivery_Pickup = 'Delivery/Pickup', _('Delivery/Pickup'),
    Product_Level = 'Product Level', _('Product Level'),


class IssueReason(models.Model):
    issue_reason_id = models.AutoField(primary_key=True)
    reason_label = models.CharField(max_length=255, null=False, blank=False, db_index=True)
    reason_type = models.CharField(
        max_length=120, db_index=True, null=False, blank=False,
        choices=IssueReasonTypeChoice.choices)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'issue_reason_mst'
        verbose_name = 'IssueReason'

    def __str__(self):
        return f"IssueReason: {self.issue_reason_id}"
