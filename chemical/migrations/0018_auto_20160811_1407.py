# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-11 14:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chemical', '0017_auto_20160811_1405'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='batch',
            name='chemical',
        ),
        migrations.RemoveField(
            model_name='batch',
            name='formula',
        ),
        migrations.DeleteModel(
            name='Batch',
        ),
    ]