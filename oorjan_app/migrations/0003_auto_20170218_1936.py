# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-18 19:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oorjan_app', '0002_auto_20170218_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solardata',
            name='dc_power',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='solarreferencedata',
            name='dc_power',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=5, null=True),
        ),
    ]
