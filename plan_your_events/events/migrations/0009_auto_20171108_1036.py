# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-08 09:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_auto_20171108_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 8, 9, 36, 26, 245932, tzinfo=utc), verbose_name='create date'),
        ),
        migrations.AlterField(
            model_name='event',
            name='mod_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 8, 9, 36, 26, 245932, tzinfo=utc), verbose_name='modification date'),
        ),
        migrations.AlterField(
            model_name='eventparticipant',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 8, 9, 36, 26, 248932, tzinfo=utc), verbose_name='create date'),
        ),
    ]
