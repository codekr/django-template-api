from django.db import models


class Zipcode(models.Model):
    zipcode = models.PositiveIntegerField(
        primary_key=True, verbose_name='Zipcode', db_index=True
    )
    city = models.CharField(
        max_length=120, db_index=True,
        verbose_name='City',
        help_text=""
    )
    state = models.CharField(
        max_length=120, db_index=True,
        verbose_name='State',
        help_text=""
    )
    lat = models.DecimalField(
        max_digits=9, decimal_places=6, db_index=True,
        verbose_name='Latitude',
        help_text=""
    )
    long = models.DecimalField(
        max_digits=9, decimal_places=6, db_index=True,
        verbose_name='Longitude',
        help_text=""
    )
    country = models.CharField(
        max_length=120, db_index=True,
        default='USA',
        verbose_name='Country',
        help_text=""
    )
    zipcode_type = models.CharField(
        max_length=30,
        verbose_name='Zipcode Type',
        help_text=""
    )
    is_decommisioned = models.BooleanField(
        default=False,
        verbose_name='Is Decommisioned',
        help_text=""
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'zipcode_mst'
        verbose_name = 'Zipcode'

    def __str__(self):
        return f"{self.zipcode} {self.city, self.state}"
