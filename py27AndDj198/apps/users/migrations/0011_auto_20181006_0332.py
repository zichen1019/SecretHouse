# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-10-06 03:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20181005_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userattr',
            name='status',
            field=models.IntegerField(blank=True, null=True, verbose_name='\u5408\u683c\u4e0e\u5426'),
        ),
    ]
