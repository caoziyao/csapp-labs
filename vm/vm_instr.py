# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/26 
@desc:
"""

from enum import Enum, unique
from zy.src.common.expression import Kind


class VMInstr(object):

    def __init__(self, op, x, y='', result=''):
        self.op = op
        self.x = x
        self.y = y
        self.result = result


class VMInstrIf(object):

    def __init__(self):
        # 基本块
        self.kind = Kind.k_if
        # self.quads = []
        self.condition = []
        self.left = []
        self.right = []


class VMInstrPrint(object):

    def __init__(self):
        # 基本块
        self.kind = Kind.print
        # self.quads = []
        self.left = []
