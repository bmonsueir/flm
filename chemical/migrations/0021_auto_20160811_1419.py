# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-11 14:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chemical', '0020_auto_20160811_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chemical',
            name='updatedAt',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='date created'),
        ),
    ]