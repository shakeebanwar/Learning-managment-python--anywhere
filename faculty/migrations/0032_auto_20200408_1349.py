# Generated by Django 3.0.4 on 2020-04-08 20:49

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0031_auto_20200407_1639'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_stories',
            name='Department_id',
        ),
        migrations.AlterField(
            model_name='teacherapplication',
            name='ApplicationDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 8, 13, 49, 47, 357070)),
        ),
        migrations.CreateModel(
            name='Query_Admin',
            fields=[
                ('queryid', models.AutoField(primary_key=True, serialize=False)),
                ('querytitle', models.CharField(default='Reason Title', max_length=50)),
                ('querymessage', models.TextField(default='Reason query', max_length=350)),
                ('querydate', models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 8, 13, 49, 47, 357070))),
                ('querystatus', models.CharField(default='Pendding', max_length=30)),
                ('Instructor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faculty.Instructor')),
            ],
        ),
    ]
