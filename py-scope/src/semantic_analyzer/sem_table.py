# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/24 
@desc:
符号表：
类型
作用域
访问控制信息
"""


class SemTable(object):

    def __init__(self):
        self.table = {}

    def enter(self, key, value):
        """
        插入
        :param key:
        :param value:
        :return:
        """
        t = self.table

        data = {
            'type': '',
            'scope': '',
        }

        t.update({
            key: value
        })

    def lookup(self, key):
        """
        查找
        :param key:
        :return:
        """
        t = self.table
        if key in t:
            return True
        else:
            return False
