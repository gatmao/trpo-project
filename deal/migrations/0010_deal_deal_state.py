# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-19 08:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deal', '0009_auto_20170916_1152'),
    ]

    operations = [
        migrations.AddField(
            model_name='deal',
            name='deal_state',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], default='1', max_length=3),
        ),
    ]