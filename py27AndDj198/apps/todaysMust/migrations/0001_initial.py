# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-11-20 22:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodaysMust',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createDate', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u521b\u5efa\u65e5\u671f')),
                ('executionTime', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6267\u884c\u65f6\u95f4')),
                ('zj', models.CharField(max_length=20, verbose_name='\u4e3b\u89d2id')),
                ('title', models.CharField(max_length=30, verbose_name='\u6807\u9898')),
                ('todaymust', models.CharField(max_length=300, verbose_name='\u5fc5\u8fbe\u4e8b\u9879')),
                ('complete', models.BooleanField(default=False, verbose_name='\u5b8c\u6210\u72b6\u6001')),
                ('sort', models.IntegerField(verbose_name='\u6392\u5e8f')),
            ],
            options={
                'verbose_name': '\u4eca\u65e5\u5fc5\u8fbe',
                'verbose_name_plural': '\u4eca\u65e5\u5fc5\u8fbe',
            },
        ),
    ]
