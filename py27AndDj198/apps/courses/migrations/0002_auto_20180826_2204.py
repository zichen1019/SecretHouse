# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-08-26 22:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='degree',
            field=models.CharField(choices=[('cj', '\u521d\u7ea7'), ('zj', '\u4e2d\u6781'), ('gj', '\u9ad8\u7ea7')], max_length=6, verbose_name='\u96be\u5ea6'),
        ),
    ]