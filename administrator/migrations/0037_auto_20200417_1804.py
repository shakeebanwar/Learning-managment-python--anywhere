# Generated by Django 3.0.4 on 2020-04-17 13:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0036_auto_20200417_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam_schedule',
            name='Year',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 17, 18, 4, 51, 349859)),
        ),
        migrations.AlterField(
            model_name='semester_schedule',
            name='Year',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 17, 18, 4, 51, 349859)),
        ),
    ]
