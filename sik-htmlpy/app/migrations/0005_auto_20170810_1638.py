# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-10 16:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_student_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='name',
        ),
        migrations.AddField(
            model_name='course',
            name='lecturers',
            field=models.TextField(default='Engr. Olaye E.'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='title',
            field=models.CharField(default='Engineering Mathematics III', help_text=b'title of course', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='test',
            name='venue',
            field=models.CharField(default='New 1000LT', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='test',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
