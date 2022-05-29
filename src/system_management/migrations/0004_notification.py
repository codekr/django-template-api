# Generated by Django 3.2.13 on 2022-05-29 05:31

from django.db import migrations, models


def forward(apps, schema_editor):
    schema_editor.execute("ALTER SEQUENCE notification_mst_notification_id_seq RESTART WITH 30000;")


def backward(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ('system_management', '0003_tax'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('notification_id', models.AutoField(primary_key=True, serialize=False)),
                ('notification_name',
                 models.CharField(db_index=True, help_text='e.g Sales & Promotions or Personalized notifications',
                                  max_length=255, verbose_name='Notification Name')),
                ('notification_channel',
                 models.CharField(choices=[('Email', 'EMAIL'), ('Push', 'PUSH'), ('Sms', 'SMS')], db_index=True,
                                  help_text='e.g Email, Sms, Push', max_length=30,
                                  verbose_name='Notification Channel')),
                ('notification_additional_text',
                 models.CharField(help_text='e.g Email Notification, Push Notification, Text Notification',
                                  max_length=255, verbose_name='Notification Channel Description')),
                ('notification_description', models.TextField(
                    help_text='e.g Our top picks among new arrivals, best-sellers and limited-time deals.',
                    max_length=255, verbose_name='Notification Description')),
                ('is_allowed_to_disabled',
                 models.BooleanField(default=False, verbose_name='Is User Allowed To Disabled?')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Notification',
                'db_table': 'notification_mst',
            },
        ),
        migrations.RunPython(forward, backward, atomic=True)
    ]
