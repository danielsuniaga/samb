# Generated by Django 4.1.2 on 2024-01-19 21:21

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0011_samb_notifications_exceptions_apis'),
    ]

    operations = [
        migrations.CreateModel(
            name='samb_notifications_exceptions_apis_independient',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=200, verbose_name='Description')),
                ('registration_date', models.CharField(max_length=14, verbose_name='Registration Date')),
                ('update_date', models.CharField(max_length=14, verbose_name='Update Date')),
                ('condition', models.CharField(max_length=1, verbose_name='Condition')),
                ('id_exceptions_api', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apis.samb_exceptions_apis')),
            ],
            options={
                'verbose_name': 'samb_notifications_exceptions_apis_independient',
                'verbose_name_plural': 'samb_notifications_exceptions_apis_independient',
                'db_table': 'samb_notifications_exceptions_apis_independient',
            },
        ),
    ]
