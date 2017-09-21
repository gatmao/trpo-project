# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-20 14:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('deal', '0013_auto_20170919_2038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deal',
            name='buyer',
        ),
        migrations.RemoveField(
            model_name='deal',
            name='seller',
        ),
        migrations.AddField(
            model_name='deal',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='deal',
            name='participant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='deals', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='deal',
            name='type',
            field=models.TextField(choices=[('buy', 'покупка'), ('sell', 'продажа')], null=True),
        ),
    ]