# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-24 05:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20170822_0454'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='company',
        ),
        migrations.DeleteModel(
            name='Company',
        ),
    ]
