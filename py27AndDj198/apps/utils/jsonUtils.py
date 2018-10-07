# -*- coding:utf-8 -*-
__author__ = 'zichen'
__create__ = '2018/10/6 11:05'

import datetime


class JsonUtils():

    def __init__(self):
        pass

    @classmethod
    def fmtDate(self, obj):
        '''
        将日期转换为json可以转换的字符串
        :param obj:
        :return:
        '''
        if issubclass(obj.__class__, list):
            return self.fmtDateList(obj)
        return obj

    @classmethod
    def fmtDateList(self, list):
        for l in list:
            if issubclass(l.__class__, dict):
                self.fmtDict(l)
        return list

    @classmethod
    def fmtDict(self, dict):
        for key,value in dict.items():
            # 此处可能因为datetime是导入的所以要使用__class__属性获取class
            if issubclass(value.__class__, datetime.__class__):
                value = value.strftime("%Y-%m-%d %H:%M:%S")
        return dict