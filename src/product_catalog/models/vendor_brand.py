from django.db import models

from .brand_mst import Brand
from .vendor_mst import Vendor


class VendorBrand(models.Model):
    vendor_brand_id = models.AutoField(primary_key=True)
    vendor = models.ForeignKey(
        Vendor, on_delete=models.CASCADE, db_index=True,
        verbose_name="Vendor Name",
        help_text=""
    )
    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE, db_index=True,
        verbose_name="Brand Name",
        help_text=""
    )
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, )
    updated_at = models.DateTimeField(auto_now=True, db_index=True, )

    class Meta:
        db_table = 'vendor_brand_link'
        verbose_name = ''
        unique_together = ('vendor_brand_id', 'vendor', 'brand',)

    def __str__(self):
        return "{}_{}".format(self.vendor.__str__(), self.brand.__str__())
