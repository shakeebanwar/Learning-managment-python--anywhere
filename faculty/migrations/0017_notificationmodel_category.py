# Generated by Django 3.0.4 on 2020-04-06 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0016_merge_20200403_2149'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificationmodel',
            name='Category',
            field=models.CharField(choices=[('class', 'Class Notification'), ('Section', 'Section Notification'), ('program', 'Program Notification')], default='', max_length=100),
        ),
    ]
