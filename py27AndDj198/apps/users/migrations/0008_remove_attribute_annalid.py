# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-10-05 12:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20181005_0023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attribute',
            name='annalid',
        ),
    ]
