# Generated by Django 3.0.4 on 2020-04-29 19:02

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0071_auto_20200420_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='ApplicationDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 30, 0, 2, 33, 888792)),
        ),
        migrations.AlterField(
            model_name='scrunityform',
            name='Date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 30, 0, 2, 33, 897767)),
        ),
        migrations.AlterField(
            model_name='student_query_admin',
            name='querydate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 30, 0, 2, 33, 894837)),
        ),
        migrations.CreateModel(
            name='Teacher_Appointment',
            fields=[
                ('Teacher_Appointment_id', models.AutoField(primary_key=True, serialize=False)),
                ('Student_Name', models.CharField(default='Name', max_length=100)),
                ('Program', models.CharField(default='Program', max_length=100)),
                ('Department', models.CharField(default='Department', max_length=100)),
                ('Course', models.CharField(default='Course', max_length=100)),
                ('Teacher', models.CharField(default='Teacher', max_length=100)),
                ('Date_Time', models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 30, 0, 2, 33, 905325))),
                ('Student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student_Profile')),
            ],
        ),
    ]
