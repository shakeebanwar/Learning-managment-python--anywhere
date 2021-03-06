# Generated by Django 3.0.4 on 2020-04-06 21:52

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0019_auto_20200406_1829'),
        ('administrator', '0001_initial'),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('ApplicationId', models.AutoField(primary_key=True, serialize=False)),
                ('ApplicationTitle', models.CharField(default='Reason Title', max_length=50)),
                ('ApplicationMessage', models.TextField(default='Reason application', max_length=350)),
                ('ApplicationAttachment', models.FileField(default='reason.pdf', upload_to='ApplicationAttachment/')),
                ('ApplicationDate', models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 6, 14, 52, 7, 943078))),
                ('ApplicationStatus', models.CharField(default='Pendding', max_length=30)),
                ('Course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faculty.Course')),
            ],
        ),
        migrations.RenameField(
            model_name='student_courses',
            old_name='Student_coursesIds',
            new_name='Student_coursesId',
        ),
        migrations.AddField(
            model_name='student_courses',
            name='Student_id',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='student.Student_Profile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student_profile',
            name='StudenBatch',
            field=models.CharField(default='Batch 1', max_length=50),
        ),
        migrations.AddField(
            model_name='student_profile',
            name='StudenShift',
            field=models.CharField(default='Morning', max_length=150),
        ),
        migrations.AlterField(
            model_name='student_courses',
            name='Samester_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrator.Samesters'),
        ),
        migrations.DeleteModel(
            name='Student_Samester',
        ),
        migrations.AddField(
            model_name='application',
            name='Student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student_Profile'),
        ),
    ]
