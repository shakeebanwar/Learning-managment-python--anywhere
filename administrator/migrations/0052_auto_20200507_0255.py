# Generated by Django 3.0.5 on 2020-05-06 21:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0051_auto_20200507_0054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam_schedule',
            name='Year',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 5, 7, 2, 55, 55, 691352)),
        ),
        migrations.AlterField(
            model_name='semester_schedule',
            name='Year',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 5, 7, 2, 55, 55, 689347)),
        ),
    ]
