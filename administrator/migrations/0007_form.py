# Generated by Django 3.0.4 on 2020-04-07 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0006_facultycalendarmodel_department_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('FormId', models.AutoField(primary_key=True, serialize=False)),
                ('FormFile', models.FileField(default='Notdata', upload_to='forms')),
                ('FileCategory', models.CharField(choices=[('facultyguidline', 'Faculty Guidline'), ('applicationform', 'Application Forms'), ('thesisguidline', 'Thesis Guidline'), ('placementforms', 'Placement Forms'), ('cacforms', 'Cac Forms')], max_length=100)),
            ],
        ),
    ]
