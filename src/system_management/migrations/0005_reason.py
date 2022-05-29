# Generated by Django 3.2.13 on 2022-05-29 05:31

from django.db import migrations, models


def forward(apps, schema_editor):
    schema_editor.execute("ALTER SEQUENCE reason_mst_reason_id_seq RESTART WITH 40000;")


def backward(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ('system_management', '0004_notification'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reason',
            fields=[
                ('reason_id', models.AutoField(primary_key=True, serialize=False)),
                ('reason_label',
                 models.TextField(db_index=True, help_text='e.g Ordering experience, Technology related',
                                  max_length=255, verbose_name='Reason Label')),
                ('reason_type',
                 models.CharField(choices=[('Product', 'Product'), ('Delivery_Pickup', 'Delivery/Pickup')],
                                  db_index=True, help_text='e.g Delivery/Pickup, Product', max_length=120,
                                  verbose_name='Reason Type')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Reason Option',
                'db_table': 'reason_mst',
            },
        ),
        migrations.RunPython(forward, backward, atomic=True)
    ]
