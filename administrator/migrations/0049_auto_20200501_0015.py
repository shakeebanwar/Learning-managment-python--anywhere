# Generated by Django 3.0.4 on 2020-04-30 19:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0048_auto_20200501_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam_schedule',
            name='Year',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 5, 1, 0, 15, 43, 238955)),
        ),
        migrations.AlterField(
            model_name='semester_schedule',
            name='Year',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 5, 1, 0, 15, 43, 237955)),
        ),
    ]
