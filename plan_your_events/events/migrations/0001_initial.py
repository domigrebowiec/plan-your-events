# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-06 22:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=50)),
                ('street_nbr', models.IntegerField(default=0)),
                ('house_nbr', models.IntegerField(default=0)),
                ('city', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('startDate', models.DateTimeField(verbose_name='start date')),
                ('endDate', models.DateTimeField(verbose_name='end date')),
                ('createDate', models.DateTimeField(verbose_name='create date')),
                ('modDate', models.DateTimeField(verbose_name='modification date')),
            ],
        ),
        migrations.CreateModel(
            name='EventParticipants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createDate', models.DateTimeField(verbose_name='create date')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Address')),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Address')),
            ],
        ),
        migrations.AddField(
            model_name='eventparticipants',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Person'),
        ),
        migrations.AddField(
            model_name='event',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Place'),
        ),
    ]