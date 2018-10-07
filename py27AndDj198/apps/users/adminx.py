# -*- coding:utf-8 -*-
__author__ = 'zichen'
__create__ = '2018/8/11 22:25'

import xadmin
from xadmin import views

from .models import EmailVeryfyRecord, Banner


# 与view绑定
class BaseSetting(object):
    # 开启主题功能
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    #页头，页脚
    site_title = 'zc Resource'
    site_footer = 'zc'
    # 收缩app中的model
    menu_style = 'accordion'


class EmailVeryfyRecordAdmin(object):
    # 显示的列表顺序同此数组中的顺序
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type', 'send_time']
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index', 'add_time']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


xadmin.site.register(EmailVeryfyRecord, EmailVeryfyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)