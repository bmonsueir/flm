# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-11 13:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chemical', '0013_auto_20160811_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formula',
            name='updatedAt',
            field=models.CharField(max_length=255),
        ),
    ]