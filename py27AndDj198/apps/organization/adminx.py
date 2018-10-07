# -*- coding:utf-8 -*-
__author__ = 'zichen'
__create__ = '2018/8/14 19:42'

from .models import CityDict, CouseOrg, Teacher
import xadmin


class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc', 'add_time']
    list_filter = ['name', 'desc', 'add_time']


class CouseOrgAdmin(object):
    list_display = ['name', 'image', 'fav_num', 'desc', 'click_num', 'city', 'address', 'add_time']
    search_fields = ['name', 'image', 'fav_num', 'desc', 'click_num', 'city', 'address', 'add_time']
    list_filter = ['name', 'image', 'fav_num', 'desc', 'click_num', 'city__name', 'address', 'add_time']


class TeacherAdmin(object):
    list_display = ['work_years', 'work_position', 'work_company', 'points', 'org', 'name',
                    'fav_num', 'click_num', 'add_time']
    search_fields = ['work_years', 'work_position', 'work_company', 'points', 'org', 'name',
                    'fav_num', 'click_num', 'add_time']
    list_filter = ['work_years', 'work_position', 'work_company', 'points', 'org__name', 'name',
                    'fav_num', 'click_num', 'add_time']


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CouseOrg, CouseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)















