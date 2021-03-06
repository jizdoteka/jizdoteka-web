# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-11 23:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0004_auto_20160306_2221'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('register', models.CharField(blank=True, default=None, max_length=20)),
                ('color', models.CharField(max_length=10)),
                ('wifi_on_board', models.BooleanField(default=False)),
                ('animals_allowed', models.BooleanField(default=False)),
                ('toll_sticker', models.BooleanField(default=False)),
                ('smoking_allowed', models.BooleanField(default=False)),
                ('air_conditioning', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='mojeid',
        ),
        migrations.AddField(
            model_name='passanger',
            name='change_timestamp',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='drive_years',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='driven_km',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='num_journeys',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='reputation',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='journey',
            name='car',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='web.Car'),
            preserve_default=False,
        ),
    ]
