# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-12 12:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0014_auto_20160212_1236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journeywaypoints',
            name='passangers',
        ),
        migrations.AddField(
            model_name='journeywaypoints',
            name='passangers',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.Passanger'),
        ),
    ]