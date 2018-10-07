# -*- coding:utf-8 -*-
__author__ = 'zichen'
__create__ = '2018/8/14 7:17'
import xadmin
from .models import Course, Lesson, Video, CourseResource


class CourseAdmin(object):
    list_display = ['add_time', 'click_num', 'degree', 'desc', 'detail', 'fav_nums', 'image', 'learn_times',
                    'name', 'student']
    search_fields = ['add_time', 'click_num', 'degree', 'desc', 'detail', 'fav_nums', 'image', 'learn_times',
                    'name', 'student']
    list_filter = ['add_time', 'click_num', 'degree', 'desc', 'detail', 'fav_nums', 'image', 'learn_times',
                    'name', 'student']


class LessonAdmin(object):
    list_display = ['add_time', 'course', 'name']
    search_fields = ['add_time', 'course', 'name']
    list_filter = ['add_time', 'course', 'name']


class VideoAdmin(object):
    list_display = ['add_time', 'lesson', 'name']
    search_fields = ['add_time', 'lesson', 'name']
    list_filter = ['add_time', 'lesson__name', 'name']


class CourseResourceAdmin(object):
    list_display = ['add_time', 'course', 'download', 'name']
    search_fields = ['add_time', 'course', 'download', 'name']
    list_filter = ['add_time', 'course_name', 'download', 'name']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)