# -*- coding:UTF-8 -*-
"""

管理员设置成了 用户：admin 密码：adminroot 邮箱：1510748736@qq.com

导包分三个区域，每个区域用空一行分割
第一区域：python自带的
第二区域：第三方库
第三区域：自己的model
"""
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name=u"昵称", default=u"")
    birday = models.DateField(verbose_name=u"生日", null=True, blank=True)
    # choices用法 如果值是men就存入男，如果man就存入女
    gender = models.CharField(max_length=6, choices=(("men",u"男"),("man",u"女")), default="men")
    addres = models.CharField(max_length=100,default=u"")
    mobile = models.CharField(max_length=11, null=True, blank=True)
    image = models.ImageField(upload_to="image/%Y/%m", default="image/default.png")

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    # 如果不重写此方法，打印中文时将乱码
    def __unicode__(self):
        return self.username


# 邮箱验证码
class EmailVeryfyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name=u"验证码")
    email = models.EmailField(max_length=50, verbose_name=u"邮箱")
    send_type = models.CharField(max_length=12, choices=(("register", u"注册"), ("forget", u"找回密码")),
                                 verbose_name=u"验证码类型")
    # datetime.now的now函数不带括号，才能调用实例化对象时的时间
    send_time = models.DateTimeField(default=datetime.now, verbose_name=u"发送时间")

    class Meta:
        verbose_name = "邮箱验证码"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '{0}({1})'.format(self.code, self.email)


# 轮播图
class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name=u"标题")
    image = models.ImageField(upload_to="banner/%Y/%m", verbose_name=u"轮播图", max_length=100)
    url = models.URLField(max_length=200, verbose_name=u"访问地址")
    index = models.IntegerField(default=100, verbose_name=u"顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = "轮播图"
        verbose_name_plural = verbose_name


class UserAttr(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u'用户')
    attrname = models.CharField(max_length=20, verbose_name=u'属性名称')
    features = models.CharField(max_length=200, verbose_name=u'评论')
    progress = models.IntegerField(default=0, verbose_name=u'评分百分比')
    index = models.IntegerField(default=100, verbose_name=u"顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    # null显示百分比 1显示成功 2显示失败
    status = models.IntegerField(null=True, blank=True, verbose_name=u'合格与否')

    class Meta:
        verbose_name = "个人属性"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.attrname