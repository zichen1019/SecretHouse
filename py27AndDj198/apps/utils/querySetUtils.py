# -*- coding:utf-8 -*-
__author__ = 'zichen'
__create__ = '2018/10/6 10:43'

from django.forms.models import model_to_dict


class QuerySetUtils:

    def __init__(self):
        pass

    @classmethod
    def ToList(self, queryset):
        '''
        将Query转换为List并返回
        :param queryset:
        :return:
        '''
        list = []
        for query in queryset:
            list.append(model_to_dict(query))
        return list

class QueryDictUtils:

    def __init__(self):
        pass

    def toBean(self, qDict, obj):
        for k, v in qDict.items():
            if k in obj.__dict__:
                # 如果变量存在，则对其赋值
                obj.__setattr__(k, v)