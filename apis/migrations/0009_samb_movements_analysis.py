# Generated by Django 4.1.2 on 2024-01-11 16:51

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0008_samb_movements'),
    ]

    operations = [
        migrations.CreateModel(
            name='samb_movements_analysis',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('registration_date', models.CharField(max_length=14, verbose_name='Registration Date')),
                ('update_date', models.CharField(max_length=14, verbose_name='Update Date')),
                ('condition', models.CharField(max_length=1, verbose_name='Condition')),
                ('id_cronjobs', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apis.samb_cronjobs')),
                ('id_movements', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apis.samb_movements')),
            ],
            options={
                'verbose_name': 'samb_movements_analysis',
                'verbose_name_plural': 'samb_movements_analysis',
                'db_table': 'samb_movements_analysis',
            },
        ),
    ]
