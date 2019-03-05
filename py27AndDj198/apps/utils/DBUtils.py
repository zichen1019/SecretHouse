# -*- coding:utf-8 -*-
__author__ = 'zichen'
__create__ = '2018/11/28 20:21'
from django.db import connection


class DbUtils:
    def __init__(self):
        cursor = connection.cursor()

    @classmethod
    def insert(self, sql):
        # 插入操作
        self.cursor.execute(sql)

    @classmethod
    def update(self, sql):
        # 更新操作
        self.cursor.execute(sql)

    @classmethod
    def delete(self, sql):
        # 删除操作
        self.cursor.execute(sql)

    @classmethod
    def selectObj(self, sql):
        # 查询操作
        self.cursor.execute(sql)
        return self.cursor.fetchone()  # 返回结果行游标直读向前，读取一条

    @classmethod
    def selectAll(self, sql):
        # 查询操作
        self.cursor.execute(sql)
        return self.cursor.fetchall()  # 读取所有