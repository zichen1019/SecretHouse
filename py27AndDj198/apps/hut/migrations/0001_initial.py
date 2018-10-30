# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-10-28 19:04
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hut',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='\u59d3\u540d')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('nanzj', models.CharField(max_length=50, verbose_name='\u7537\u4e3b\u89d2ID')),
                ('nvzj', models.CharField(max_length=50, verbose_name='\u5973\u4e3b\u89d2ID')),
                ('key', models.CharField(max_length=50, verbose_name='\u79d8\u94a5')),
                ('priority', models.CharField(max_length=10, verbose_name='\u4f18\u5148\u7ea7')),
            ],
            options={
                'verbose_name': '\u5c0f\u5c4b',
                'verbose_name_plural': '\u5c0f\u5c4b',
            },
        ),
    ]