# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-10 07:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='duration',
            field=models.PositiveIntegerField(default=90),
            preserve_default=False,
        ),
    ]
