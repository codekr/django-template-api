from django.db import models


class Vendor(models.Model):
    vendor_id = models.AutoField(primary_key=True)
    qb_id = models.CharField(max_length=30, null=True, blank=True, db_index=True, )
    vendor_company_name = models.CharField(max_length=255, null=True, blank=True, db_index=True, )
    vendor_address = models.CharField(max_length=255, null=True, blank=True)
    vendor_address2 = models.CharField(max_length=255, null=True, blank=True)
    vendor_city = models.CharField(max_length=50, null=True, blank=True)
    vendor_zip_pin_code = models.CharField(max_length=15, null=True, blank=True)
    vendor_country = models.CharField(max_length=50, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, db_index=True, )
    updated_at = models.DateTimeField(auto_now=True, db_index=True, )

    class Meta:
        db_table = 'vendors'
        verbose_name = 'Vendor'

    def __str__(self):
        return f"{self.vendor_company_name}"
