# Generated by Django 3.0.4 on 2020-04-17 07:39

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0057_auto_20200417_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='ApplicationDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 17, 12, 39, 7, 499820)),
        ),
        migrations.AlterField(
            model_name='scrunityform',
            name='Date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 17, 12, 39, 7, 499820)),
        ),
        migrations.AlterField(
            model_name='student_query_admin',
            name='querydate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 17, 12, 39, 7, 499820)),
        ),
        migrations.CreateModel(
            name='Student_Surver_Answer',
            fields=[
                ('Student_Surver_Answer', models.AutoField(primary_key=True, serialize=False)),
                ('question_1_Answer', models.CharField(default='agree', max_length=10)),
                ('question_2_Answer', models.CharField(default='strongagree', max_length=10)),
                ('Student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student_Profile')),
            ],
        ),
    ]
