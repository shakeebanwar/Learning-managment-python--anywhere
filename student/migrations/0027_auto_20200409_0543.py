# Generated by Django 3.0.4 on 2020-04-09 12:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0026_auto_20200409_0540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='ApplicationDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 9, 5, 43, 32, 62023)),
        ),
    ]
