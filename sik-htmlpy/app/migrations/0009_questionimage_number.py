# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-16 03:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_question_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionimage',
            name='number',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]