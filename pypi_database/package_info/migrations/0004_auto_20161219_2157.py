# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-19 21:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('package_info', '0003_packageinfo_development_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='packageinfo',
            name='has_classifiers',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='packageinfo',
            name='python3_compatible',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
