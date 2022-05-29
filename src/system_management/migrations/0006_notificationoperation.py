# Generated by Django 3.2.13 on 2022-05-29 05:31

from django.db import migrations, models
import django_quill.fields


def forward(apps, schema_editor):
    schema_editor.execute("ALTER SEQUENCE notification_operation_mst_notification_operation_id_seq RESTART WITH 50000;")


def backward(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('system_management', '0005_reason'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationOperation',
            fields=[
                ('notification_operation_id', models.AutoField(primary_key=True, serialize=False)),
                ('area', models.CharField(choices=[('Orders', 'Orders'), ('Refunds', 'Refunds'), ('Catalog', 'Catalog')], db_index=True, help_text='Note: E.g. Order, Refund, Product', max_length=120, verbose_name='Notification Area')),
                ('trigger_action', models.CharField(choices=[('NEW_ORDER', 'When New Order Placed'), ('DAILY_ORDER', 'Daily Order Value')], db_index=True, max_length=255, verbose_name='Notification Trigger On')),
                ('type', models.CharField(choices=[('Sms', 'SMS'), ('Email', 'EMAIL'), ('Email_Sms', 'EMAIL/SMS')], db_index=True, max_length=255, verbose_name='Notification Channel')),
                ('sms_content', models.TextField(blank=True, help_text='Note: Text message content either templating or plain text', max_length=255, null=True, verbose_name='SMS Message Content')),
                ('email_content', django_quill.fields.QuillField(blank=True, help_text='Note: Email message content either templating or plain text', null=True, verbose_name='Email Message Content')),
                ('frequency', models.PositiveSmallIntegerField(blank=True, db_index=True, default=1, null=True, verbose_name='Notification Frequency')),
                ('time', models.TimeField(blank=True, db_index=True, null=True, verbose_name='At Time')),
                ('email_recipient', models.TextField(blank=True, help_text='Note: Comma separated email address, e.g dinesh@radiansys.com, dheeraj@radiansys.com', max_length=1000, null=True, verbose_name="Recipient's Email Addresses")),
                ('sms_recipient', models.TextField(blank=True, help_text='Note: Comma separated phone number including country code, e.g +1543678909, +9187676545656', max_length=1000, null=True, verbose_name="Recipient's Phone Numbers")),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Notification Operation',
                'db_table': 'notification_operation_mst',
            },
        ),
        migrations.RunPython(forward, backward, atomic=True)
    ]
