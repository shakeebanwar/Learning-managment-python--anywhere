# Generated by Django 3.0.4 on 2020-04-02 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0008_instructor_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instructor',
            name='username',
        ),
    ]
