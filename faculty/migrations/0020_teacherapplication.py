# Generated by Django 3.0.4 on 2020-04-07 07:11

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0019_auto_20200406_1829'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherApplication',
            fields=[
                ('ApplicationId', models.AutoField(primary_key=True, serialize=False)),
                ('ApplicationTitle', models.CharField(default='Reason Title', max_length=50)),
                ('ApplicationMessage', models.TextField(default='Reason application', max_length=350)),
                ('ApplicationAttachment', models.FileField(default='reason.pdf', upload_to='ApplicationAttachment/')),
                ('ApplicationDate', models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 7, 12, 11, 37, 577402))),
                ('ApplicationStatus', models.CharField(default='Pendding', max_length=30)),
                ('Instructor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faculty.Instructor')),
            ],
        ),
    ]
