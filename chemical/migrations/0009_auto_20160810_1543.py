# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-10 15:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chemical', '0008_auto_20160810_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attribute',
            name='updatedAt',
            field=models.DateTimeField(default=1, verbose_name='date created'),
        ),
        migrations.AlterField(
            model_name='specification',
            name='updatedAt',
            field=models.DateTimeField(default=1, verbose_name='date created'),
        ),
    ]
