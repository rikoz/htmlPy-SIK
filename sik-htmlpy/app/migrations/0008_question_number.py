# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-16 02:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20170816_0158'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='number',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]