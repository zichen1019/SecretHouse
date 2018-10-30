# _*_ encoding:UTF-8 _*_
from __future__ import unicode_literals

from datetime import datetime

from django.db import models

from users.models import UserProfile
from courses.models import Course

# Create your models here.


class Hut(models.Model):
    name = models.CharField(max_length=20, verbose_name=u"姓名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    nanzj = models.CharField(max_length=50, verbose_name=u"男主角ID")
    nvzj = models.CharField(max_length=50, verbose_name=u"女主角ID")
    key = models.CharField(max_length=50, verbose_name=u"秘钥")
    priority = models.CharField(max_length=10, verbose_name=u"优先级")

    class Meta:
        verbose_name = "小屋"
        verbose_name_plural = verbose_name
