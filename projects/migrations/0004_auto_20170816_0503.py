# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-16 05:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0003_auto_20170816_0458'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='ProjectMember',
            new_name='Member',
        ),
        migrations.AddField(
            model_name='log',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Member'),
        ),
        migrations.AddField(
            model_name='log',
            name='worker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
