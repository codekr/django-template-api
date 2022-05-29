from django.db import models
from django.utils.translation import gettext_lazy as _


class LegalTermTypeChoice(models.TextChoices):
    Terms_Of_Service = 'Terms_Of_Service', _('Terms of service'),
    Privacy = 'Privacy', _('Privacy'),
    Membership = 'Membership', _('Membership'),
    Payment_Terms = 'Payment_Terms', _('Payment terms')


class LegalTerm(models.Model):
    legal_terms_id = models.AutoField(primary_key=True)
    term_type = models.CharField(
        max_length=30, db_index=True,
        choices=LegalTermTypeChoice.choices,
        verbose_name="Terms Type",
        help_text=""
    )
    legal_file_name = models.CharField(
        max_length=255,
        verbose_name="Filename",
        help_text=""
    )
    effective_from = models.DateField(
        verbose_name="Effective From",
        help_text=""
    )
    version = models.CharField(
        max_length=20,
        verbose_name="Version",
        help_text=""
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'legal_terms_mst'
        verbose_name = 'Legal Term'

    def __str__(self):
        return f"Legal Terms: {self.legal_terms_id}"
