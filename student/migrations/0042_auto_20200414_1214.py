# Generated by Django 3.0.4 on 2020-04-14 07:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0041_auto_20200414_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='ApplicationDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 14, 12, 14, 1, 888515)),
        ),
    ]
