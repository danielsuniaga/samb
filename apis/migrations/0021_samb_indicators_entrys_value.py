# Generated by Django 4.1.2 on 2024-02-16 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0020_samb_indicators_samb_indicators_entrys'),
    ]

    operations = [
        migrations.AddField(
            model_name='samb_indicators_entrys',
            name='value',
            field=models.CharField(default='0', max_length=14, verbose_name='Value'),
        ),
    ]
