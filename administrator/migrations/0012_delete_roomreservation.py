# Generated by Django 3.0.4 on 2020-04-09 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0011_rooms_roomcode'),
    ]

    operations = [
        migrations.DeleteModel(
            name='RoomReservation',
        ),
    ]
