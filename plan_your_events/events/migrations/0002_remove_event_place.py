# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-07 21:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='place',
        ),
    ]
