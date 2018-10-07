# -*- coding:utf-8 -*-
__author__ = 'zichen'
__create__ = '2018/10/6 10:43'

from django.forms.models import model_to_dict


class QuerySetUtils():

    def __init__(self):
        pass

    @classmethod
    def ToList(self, querySet):
        '''
        将Query转换为List并返回
        :param querySet:
        :return:
        '''
        list = []
        for query in querySet:
            list.append(model_to_dict(query))
        return list