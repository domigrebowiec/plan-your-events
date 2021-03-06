# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-07 21:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20171107_2246'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='createDate',
            new_name='create_date',
        ),
        migrations.RemoveField(
            model_name='event',
            name='endDate',
        ),
        migrations.RemoveField(
            model_name='event',
            name='modDate',
        ),
        migrations.RemoveField(
            model_name='event',
            name='startDate',
        ),
        migrations.RemoveField(
            model_name='eventparticipant',
            name='createDate',
        ),
        migrations.AddField(
            model_name='event',
            name='end_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='end date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='mod_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='modification date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='start_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='start date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='eventparticipant',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='create date'),
            preserve_default=False,
        ),
    ]
