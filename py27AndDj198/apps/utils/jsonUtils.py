# -*- coding:utf-8 -*-
__author__ = 'zichen'
__create__ = '2018/10/6 11:05'

from datetime import datetime


class JsonDateUtils():

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
        elif issubclass(obj.__class__, dict):
            return self.fmtDict(obj)
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
            if issubclass(value.__class__, datetime):
                value = value.strftime("%Y-%m-%d %H:%M:%S")
        return dict


class JsonToBeanUtils():

    def __init__(self):
        pass

    @classmethod
    def jsonToBean(self, json, obj):
        """
        将json数据转换为对象
        :param json: json数据
        :param obj: 将要赋值对象
        :return:
        """
        # 遍历出json的所有key与value
        for k, v in json.items():
            # 判断对象中是否有此变量
            if k in obj.__dict__:
                # 如果变量存在，则对其赋值
                obj.__setattr__(k, v)