# Generated by Django 3.0.4 on 2020-04-09 08:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0021_auto_20200408_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='ApplicationDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 9, 1, 34, 55, 492990)),
        ),
    ]
