# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-11 14:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chemical', '0016_auto_20160811_1356'),
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phase', models.CharField(max_length=5)),
                ('amount', models.DecimalField(decimal_places=4, default=0.0, max_digits=5)),
                ('instruction', models.CharField(max_length=255)),
                ('row', models.IntegerField()),
                ('updatedBy', models.CharField(max_length=255)),
                ('permissions', models.CharField(max_length=255)),
                ('updatedAt', models.DateTimeField(default=datetime.datetime.now, verbose_name='date created')),
                ('chemical', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chemical.Chemical')),
            ],
        ),
        migrations.RemoveField(
            model_name='formula',
            name='attribute',
        ),
        migrations.RemoveField(
            model_name='formula',
            name='references',
        ),
        migrations.RemoveField(
            model_name='formula',
            name='value',
        ),
        migrations.RemoveField(
            model_name='project',
            name='attribute',
        ),
        migrations.RemoveField(
            model_name='project',
            name='references',
        ),
        migrations.RemoveField(
            model_name='project',
            name='value',
        ),
        migrations.AddField(
            model_name='formula',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='chemical.Project'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='formula',
            name='updatedAt',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='date created'),
        ),
        migrations.AlterField(
            model_name='project',
            name='updatedAt',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='date created'),
        ),
        migrations.AddField(
            model_name='batch',
            name='formula',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chemical.Formula'),
        ),
    ]
