# -*- coding:utf-8 -*-
__author__ = 'zichen'
__create__ = '2018/8/14 19:42'

from .models import UserAsk, CourseComments, UserFavorite, UserMessage, UserCourse
import xadmin


class UserAskAdmin(object):
    list_display = ['name', 'mobile', 'course_name', 'add_time']
    search_fields = ['name', 'mobile', 'course_name', 'add_time']
    list_filter = ['name', 'mobile', 'course_name', 'add_time']


class CourseCommentsAdmin(object):
    list_display = ['user', 'course', 'comments', 'add_time']
    search_fields = ['user', 'course', 'comments', 'add_time']
    list_filter = ['user__name', 'course__name', 'comments', 'add_time']


class UserFavoriteAdmin(object):
    list_display = ['user', 'fav_type', 'fav_id', 'add_time']
    search_fields = ['user', 'fav_type', 'fav_id', 'add_time']
    list_filter = ['user__name', 'fav_type', 'fav_id', 'add_time']


class UserMessageAdmin(object):
    list_display = ['user', 'message', 'has_read', 'add_time']
    search_fields = ['user', 'message', 'has_read', 'add_time']
    list_filter = ['user__name', 'message', 'has_read', 'add_time']


class UserCourseAdmin(object):
    list_display = ['user', 'course', 'add_time']
    search_fields = ['user', 'course', 'add_time']
    list_filter = ['user__name', 'course__name', 'add_time']


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(CourseComments, CourseCommentsAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)