# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-11 14:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chemical', '0019_auto_20160811_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='row',
            field=models.IntegerField(default=1),
        ),
    ]