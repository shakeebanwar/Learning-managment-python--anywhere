# Generated by Django 3.0.4 on 2020-04-09 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0014_menu'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuOrders',
            fields=[
                ('OrderId', models.AutoField(primary_key=True, serialize=False)),
                ('OrderList', models.TextField(default='Comments', max_length=450)),
                ('OrderStartDate', models.DateField()),
                ('OrderStartTime', models.TimeField()),
                ('OrderEndTime', models.TimeField()),
                ('MenuId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrator.menu')),
            ],
        ),
    ]
