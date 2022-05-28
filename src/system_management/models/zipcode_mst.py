from django.db import models


class ZipCode(models.Model):
    zipcode = models.PositiveIntegerField(primary_key=True, verbose_name='Zipcode', db_index=True)
    city = models.CharField(max_length=120, db_index=True, verbose_name='City')
    state = models.CharField(max_length=120, db_index=True, verbose_name='State')
    lat = models.DecimalField(max_digits=9, decimal_places=6, db_index=True, verbose_name='Latitude')
    long = models.DecimalField(max_digits=9, decimal_places=6, db_index=True, verbose_name='Longitude')
    country = models.CharField(max_length=120, db_index=True, verbose_name='Country', default='USA')
    zipcode_type = models.CharField(max_length=30, verbose_name='Zipcode Type')
    is_decommisioned = models.BooleanField(default=False, verbose_name='Is Decommisioned')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'zipcode_mst'
        verbose_name = 'Zipcode'

    def __str__(self):
        return f"{self.zipcode} {self.city, self.state}"
