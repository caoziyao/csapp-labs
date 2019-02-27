# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/12/14 
@desc:
"""


class CommonVar(object):
    index = 0
    _instance = None

    def __new__(cls, *args, **kw):
        if not cls._instance:
            cls._instance = super(CommonVar, cls).__new__(cls, *args, **kw)
        return cls._instance

    def get_tmp_var(self):
        t = '#{}'.format(self.index)
        self.index += 1
        return t


class BaseIR(object):
    pass
