# Generated by Django 3.0.4 on 2020-04-14 07:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0042_auto_20200414_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='ApplicationDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 14, 12, 18, 18, 300433)),
        ),
    ]
