# Generated by Django 3.2.13 on 2022-05-29 12:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('system_management', '0007_auto_20220529_0553'),
    ]

    operations = [
        migrations.RenameField(
            model_name='zipcode',
            old_name='zipcode_type',
            new_name='type',
        ),
        migrations.RemoveField(
            model_name='zipcode',
            name='city',
        ),
        migrations.AddField(
            model_name='zipcode',
            name='name',
            field=models.CharField(db_index=True, default=django.utils.timezone.now, max_length=120, verbose_name='Zipcode Name'),
            preserve_default=False,
        ),
    ]