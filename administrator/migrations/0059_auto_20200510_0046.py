# Generated by Django 3.0.4 on 2020-05-09 19:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0058_auto_20200509_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam_schedule',
            name='Year',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 5, 10, 0, 46, 53, 278377)),
        ),
        migrations.AlterField(
            model_name='semester_schedule',
            name='Year',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 5, 10, 0, 46, 53, 277163)),
        ),
    ]
