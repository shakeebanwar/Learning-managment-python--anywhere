# Generated by Django 3.0.4 on 2020-04-16 13:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0058_auto_20200416_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query_admin',
            name='querydate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 16, 18, 35, 29, 672600)),
        ),
        migrations.AlterField(
            model_name='teacherapplication',
            name='ApplicationDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 16, 18, 35, 29, 670599)),
        ),
    ]
