# Generated by Django 3.0.4 on 2020-05-13 19:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0098_auto_20200510_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query_admin',
            name='querydate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 5, 14, 0, 1, 17, 613595)),
        ),
        migrations.AlterField(
            model_name='teacherapplication',
            name='ApplicationDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 5, 14, 0, 1, 17, 610592)),
        ),
    ]
