# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-08 09:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_auto_20171108_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='create date'),
        ),
        migrations.AlterField(
            model_name='event',
            name='mod_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='modification date'),
        ),
        migrations.AlterField(
            model_name='eventparticipant',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='create date'),
        ),
    ]