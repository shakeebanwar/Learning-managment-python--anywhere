# Generated by Django 3.0.4 on 2020-04-07 10:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0014_auto_20200407_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='ApplicationDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 7, 15, 50, 14, 193862)),
        ),
    ]
