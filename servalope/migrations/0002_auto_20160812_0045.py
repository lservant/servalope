# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-12 00:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('servalope', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailing',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='mailing',
            name='message',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
