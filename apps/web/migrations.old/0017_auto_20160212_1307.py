# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-12 13:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0016_auto_20160212_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journeywaypoints',
            name='passangers',
            field=models.ManyToManyField(blank=True, to='web.Passanger'),
        ),
    ]