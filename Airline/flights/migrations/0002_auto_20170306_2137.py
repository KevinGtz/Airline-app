# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-07 03:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='flight_name',
            field=models.CharField(default=False, max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='arrival_city',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='departure_city',
            field=models.CharField(max_length=100),
        ),
    ]
