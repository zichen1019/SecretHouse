# -*- coding:utf-8 -*-
__author__ = 'zichen'
__create__ = '2018/11/14 21:24'
from django.db import models
from datetime import datetime


class TodaysMust(models.Model):

    createDate = models.DateTimeField(default=datetime.now, verbose_name=u'创建日期')
    executionTime = models.DateTimeField(default=datetime.now, verbose_name=u'执行时间')
    zj = models.CharField(max_length=20, verbose_name=u'主角id')
    title = models.CharField(max_length=30, verbose_name=u'标题')
    todaymust = models.CharField(max_length=300, verbose_name=u'必达事项')
    complete = models.BooleanField(default=False, verbose_name=u'完成状态')
    sort = models.IntegerField(verbose_name=u'排序')

    class Meta:
        verbose_name = u'今日必达'
        verbose_name_plural = verbose_name

