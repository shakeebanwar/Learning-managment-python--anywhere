# Generated by Django 3.0.4 on 2020-04-10 18:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0045_auto_20200410_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query_admin',
            name='querydate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 10, 23, 20, 7, 17355)),
        ),
        migrations.AlterField(
            model_name='teacherapplication',
            name='ApplicationDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 10, 23, 20, 7, 14371)),
        ),
    ]
