from django.db import models


class Vendor(models.Model):
    vendor_id = models.AutoField(primary_key=True)
    qb_id = models.CharField(
        max_length=30, null=True, blank=True, db_index=True,
        verbose_name="Quickbook ID",
        help_text="Note: Quickbook vendor linking ID."
    )
    company_name = models.CharField(
        max_length=255, db_index=True,
        verbose_name="Name",
        help_text=""
    )
    address = models.CharField(
        max_length=255,
        verbose_name="Street",
        help_text=""
    )
    address2 = models.CharField(
        max_length=255, null=True, blank=True,
        verbose_name="Address",
        help_text=""
    )
    city = models.CharField(
        max_length=50,
        verbose_name="City",
        help_text=""
    )
    zip_pin_code = models.CharField(
        max_length=15,
        verbose_name="Zipcode",
        help_text=""
    )
    country = models.CharField(
        max_length=50,
        verbose_name="Country",
        help_text=""
    )

    created_at = models.DateTimeField(auto_now_add=True, db_index=True, )
    updated_at = models.DateTimeField(auto_now=True, db_index=True, )

    class Meta:
        db_table = 'vendor_mst'
        verbose_name = 'Vendor'

    def __str__(self):
        return f"{self.company_name}"
