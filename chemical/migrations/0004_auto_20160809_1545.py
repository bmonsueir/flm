# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-09 15:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chemical', '0003_formula_project'),
    ]

    operations = [
        migrations.RenameField(
            model_name='specification',
            old_name='attribute',
            new_name='max_value',
        ),
        migrations.RenameField(
            model_name='specification',
            old_name='references',
            new_name='min_value',
        ),
        migrations.RenameField(
            model_name='specification',
            old_name='value',
            new_name='test_method',
        ),
    ]
