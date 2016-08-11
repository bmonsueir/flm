# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-11 13:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chemical', '0015_auto_20160811_1348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formula',
            name='project',
        ),
        migrations.AddField(
            model_name='formula',
            name='attribute',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formula',
            name='references',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formula',
            name='value',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='attribute',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='references',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='value',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
