# Generated by Django 3.0.5 on 2020-05-08 18:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0081_auto_20200508_0256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='ApplicationDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 5, 8, 23, 25, 4, 864067)),
        ),
        migrations.AlterField(
            model_name='scrunityform',
            name='Date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 5, 8, 23, 25, 4, 869084)),
        ),
        migrations.AlterField(
            model_name='student_assigment',
            name='Date_Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 5, 8, 23, 25, 4, 874066)),
        ),
        migrations.AlterField(
            model_name='student_query_admin',
            name='querydate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 5, 8, 23, 25, 4, 869084)),
        ),
        migrations.AlterField(
            model_name='teacher_appointment',
            name='Date_Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 5, 8, 23, 25, 4, 874066)),
        ),
    ]
