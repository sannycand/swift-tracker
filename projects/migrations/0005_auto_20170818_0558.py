# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-18 05:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20170816_0503'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='log',
            name='worker',
        ),
        migrations.AlterField(
            model_name='log',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]