# Generated by Django 3.0.1 on 2020-03-26 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_events_eventtitle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='eventendtime',
        ),
        migrations.RemoveField(
            model_name='events',
            name='eventstarttime',
        ),
    ]
