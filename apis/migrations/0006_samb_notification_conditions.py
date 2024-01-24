# Generated by Django 4.1.2 on 2024-01-11 16:50

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0005_samb_cronjobs'),
    ]

    operations = [
        migrations.CreateModel(
            name='samb_notification_conditions',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100, verbose_name='Description')),
                ('registration_date', models.CharField(max_length=14, verbose_name='Registration Date')),
                ('update_date', models.CharField(max_length=14, verbose_name='Update Date')),
                ('condition', models.CharField(max_length=1, verbose_name='Condition')),
                ('id_samb_cronjobs', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apis.samb_cronjobs')),
            ],
            options={
                'verbose_name': 'samb_notification_conditions',
                'verbose_name_plural': 'samb_notification_conditions',
                'db_table': 'samb_notification_conditions',
            },
        ),
    ]
