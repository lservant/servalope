# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-12 00:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(blank=True, max_length=100)),
                ('middle', models.CharField(blank=True, max_length=100)),
                ('last', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('rsvp', models.CharField(choices=[('Y', 'Yes'), ('M', 'Maybe'), ('N', 'No')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField(default=datetime.datetime.today)),
            ],
        ),
        migrations.AddField(
            model_name='guest',
            name='mailing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servalope.Mailing'),
        ),
    ]
