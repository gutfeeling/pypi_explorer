# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-22 22:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('package_info', '0007_auto_20161220_1716'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='packageinfo',
            name='description_length',
        ),
        migrations.RemoveField(
            model_name='packageinfo',
            name='first_release_date',
        ),
        migrations.RemoveField(
            model_name='packageinfo',
            name='number_of_releases',
        ),
        migrations.RemoveField(
            model_name='packageinfo',
            name='quality_factor',
        ),
        migrations.AddField(
            model_name='packageinfo',
            name='keywords',
            field=models.TextField(null=True),
        ),
    ]
