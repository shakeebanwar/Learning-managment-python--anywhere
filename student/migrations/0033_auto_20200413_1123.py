# Generated by Django 3.0.4 on 2020-04-13 06:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0032_auto_20200410_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='ApplicationDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 13, 11, 23, 51, 163157)),
        ),
    ]
