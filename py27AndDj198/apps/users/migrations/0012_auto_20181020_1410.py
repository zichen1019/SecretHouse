# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-10-20 14:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20181006_0332'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='ipaddr',
            field=models.GenericIPAddressField(blank=True, null=True, verbose_name='\u767b\u5f55IP'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='token',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='\u9a8c\u8bc1'),
        ),
    ]
