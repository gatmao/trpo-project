# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-19 13:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deal', '0012_auto_20170919_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deal',
            name='deal_state',
            field=models.CharField(choices=[('pending', 'pending'), ('accepted', 'accepted'), ('rejected', 'rejected')], default='pending', max_length=10),
        ),
    ]
