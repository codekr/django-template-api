from django.db import models

from .cuisine_mst import Cuisine
from .region_mst import Region


class RegionCuisine(models.Model):
    region_cuisine_id = models.AutoField(primary_key=True)
    region = models.ForeignKey(
        Region, on_delete=models.CASCADE, db_index=True,
        verbose_name="Region Name",
        help_text=""
    )
    cuisine = models.ForeignKey(
        Cuisine, on_delete=models.CASCADE, db_index=True,
        verbose_name="Cuisine Name",
        help_text=""
    )
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, )
    updated_at = models.DateTimeField(auto_now=True, db_index=True, )

    class Meta:
        db_table = 'region_cuisine_id'
        verbose_name = ''
        unique_together = ('region_cuisine_id', 'region', 'cuisine',)

    def __str__(self):
        return "{}_{}".format(self.region.__str__(), self.cuisine.__str__())
