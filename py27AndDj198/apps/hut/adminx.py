# -*- coding:utf-8 -*-
__author__ = 'zichen'
__create__ = '2018/8/14 19:42'

from .models import Hut
import xadmin


class HutAdmin(object):
    list_display = ['name', 'nanzj', 'nvzj', 'add_time']
    search_fields = ['name', 'nanzj', 'nvzj', 'add_time']
    list_filter = ['name', 'nanzj', 'nvzj', 'add_time']


xadmin.site.register(Hut, HutAdmin)