# Generated by Django 3.2.13 on 2022-05-29 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_catalog', '0013_categorysubcategory'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categorysubcategory',
            options={'verbose_name': 'Category Sub Category', 'verbose_name_plural': 'Category Sub Categories'},
        ),
        migrations.AddField(
            model_name='category',
            name='sub_categories',
            field=models.ManyToManyField(db_index=True, through='product_catalog.CategorySubCategory', to='product_catalog.SubCategory'),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='categories',
            field=models.ManyToManyField(db_index=True, through='product_catalog.CategorySubCategory', to='product_catalog.Category'),
        ),
    ]
