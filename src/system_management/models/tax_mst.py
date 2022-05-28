from django.db import models
from .zipcode_mst import ZipCode


class Tax(models.Model):
    tax_rate_id = models.AutoField(primary_key=True)
    zipcode = models.OneToOneField(ZipCode, on_delete=models.CASCADE)
    state_rate = models.DecimalField(max_digits=9, decimal_places=6, db_index=True, verbose_name='State Tax Rate')
    county_rate = models.DecimalField(max_digits=9, decimal_places=6, db_index=True, verbose_name='County Tax Rate')
    special_rate = models.DecimalField(max_digits=9, decimal_places=6, db_index=True, verbose_name='Special Rate')
    combined_district_rate = models.DecimalField(
        max_digits=9, decimal_places=3, db_index=True,
        verbose_name='Combined District Tax Rate'
    )
    is_freight_taxable = models.BooleanField(default=False, verbose_name="Is Freight Taxable?")
    status = models.CharField(max_length=40, verbose_name='Status')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tax_mst'
        verbose_name = 'Tax'

    def __str__(self):
        return f"Tax: {self.tax_rate_id}"
