# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-20 12:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('package_info', '0004_auto_20161219_2157'),
    ]

    operations = [
        migrations.RenameField(
            model_name='packageinfo',
            old_name='last_release_size',
            new_name='last_release_size_source',
        ),
        migrations.AddField(
            model_name='packageinfo',
            name='last_release_size_wheel',
            field=models.IntegerField(null=True),
        ),
    ]
