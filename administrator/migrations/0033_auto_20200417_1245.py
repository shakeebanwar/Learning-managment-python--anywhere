# Generated by Django 3.0.4 on 2020-04-17 07:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0032_auto_20200417_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam_schedule',
            name='Year',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 17, 12, 45, 21, 729172)),
        ),
        migrations.AlterField(
            model_name='semester_schedule',
            name='Year',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 17, 12, 45, 21, 729172)),
        ),
    ]
