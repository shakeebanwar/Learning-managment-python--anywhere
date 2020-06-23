# Generated by Django 3.0.4 on 2020-03-29 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instructor', '0009_auto_20200323_1548'),
    ]

    operations = [
        migrations.CreateModel(
            name='videos',
            fields=[
                ('vid', models.AutoField(primary_key=True, serialize=False)),
                ('videoTitle', models.CharField(default='Video Title', max_length=250)),
                ('videoFile', models.FileField(default='test.jpg', upload_to='videos/')),
                ('courseId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instructor.Course')),
            ],
        ),
    ]
