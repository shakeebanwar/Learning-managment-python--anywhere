# Generated by Django 3.0.4 on 2020-04-17 06:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0022_semester_schedule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semester_schedule',
            name='Year',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 17, 11, 18, 36, 596159)),
        ),
    ]
