# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-05 13:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deal', '0003_auto_20170905_2048'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deal',
            old_name='customer',
            new_name='buyer',
        ),
    ]
