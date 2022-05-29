# Generated by Django 3.2.13 on 2022-05-29 15:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('product_catalog', '0007_vendorbrand'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='vendors',
            field=models.ManyToManyField(db_index=True, through='product_catalog.VendorBrand',
                                         to='product_catalog.Vendor'),
        ),
        migrations.AddField(
            model_name='vendor',
            name='brands',
            field=models.ManyToManyField(db_index=True, through='product_catalog.VendorBrand',
                                         to='product_catalog.Brand'),
        ),
    ]