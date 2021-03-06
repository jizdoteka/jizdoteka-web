# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-12 11:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_auto_20160212_1128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='waypoint',
            name='output_only',
        ),
        migrations.AddField(
            model_name='journeywaypoints',
            name='output_only',
            field=models.BooleanField(default=False, help_text='Waypoting is for leaving only.'),
        ),
        migrations.AlterField(
            model_name='journeywaypoints',
            name='passangers',
            field=models.ManyToManyField(blank=True, to='web.Passanger'),
        ),
    ]
