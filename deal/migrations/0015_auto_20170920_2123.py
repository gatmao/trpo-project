# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-20 14:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deal', '0014_auto_20170920_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deal',
            name='deal_state',
            field=models.TextField(choices=[('pending', 'pending'), ('accepted', 'accepted'), ('rejected', 'rejected')], default='pending'),
        ),
    ]
