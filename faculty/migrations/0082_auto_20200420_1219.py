# Generated by Django 3.0.4 on 2020-04-20 07:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0081_auto_20200420_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query_admin',
            name='querydate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 20, 12, 19, 54, 316108)),
        ),
        migrations.AlterField(
            model_name='teacherapplication',
            name='ApplicationDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 20, 12, 19, 54, 314111)),
        ),
    ]
