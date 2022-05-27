from django.db import models
from django.contrib.postgres.fields import JSONField


class Brand(models.Model):
    brand_id = models.AutoField(primary_key=True)
    brand_name = models.CharField(max_length=255, null=True, blank=True, )
    brand_logo_image_id = models.CharField(max_length=255, null=True, blank=True, )
    is_exclusive = models.BooleanField(default=False)
    is_recognised_brand = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)

    deleted_at = models.DateTimeField(null=True, blank=True, )
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, )
    updated_at = models.DateTimeField(auto_now=True, db_index=True, )
    created_by = models.CharField(max_length=40, null=True, blank=True, )
    updated_by = models.CharField(max_length=40, null=True, blank=True, )
    created_by_ip = models.CharField(max_length=40, null=True, blank=True, )
    updated_by_ip = models.CharField(max_length=40, null=True, blank=True, )

    class Meta:
        db_table = 'brands',
        verbose_name = 'Brand'
