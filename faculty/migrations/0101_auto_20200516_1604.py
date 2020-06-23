# Generated by Django 3.0.4 on 2020-05-16 11:04

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0100_auto_20200514_0223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query_admin',
            name='querydate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 5, 16, 16, 4, 46, 852940)),
        ),
        migrations.AlterField(
            model_name='teacherapplication',
            name='ApplicationDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 5, 16, 16, 4, 46, 852001)),
        ),
        migrations.CreateModel(
            name='onlinequiz',
            fields=[
                ('onlinequizid', models.AutoField(primary_key=True, serialize=False)),
                ('semester', models.CharField(default='', max_length=100)),
                ('quizlink', models.CharField(default='link', max_length=1000)),
                ('Course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faculty.Course')),
                ('Department_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faculty.Department')),
                ('Instructor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faculty.Instructor')),
            ],
        ),
    ]
