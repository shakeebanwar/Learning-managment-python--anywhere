# Generated by Django 3.0.4 on 2020-04-07 10:18

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0027_auto_20200407_1518'),
        ('student', '0012_auto_20200407_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='Instructor_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='faculty.Instructor'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='application',
            name='ApplicationDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 7, 15, 17, 59, 616987)),
        ),
    ]
