# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/23
@desc:
三地址码
"""

from enum import Enum, unique
from zy.src.common.expression import Kind


# @unique
# class InstrKind(Enum):
#     const = 0
#     move = 1
#     plus = 2
#     assignment = 3
#     k_if = 4


class InstrT(object):

    def __init__(self, instr_kind):
        self.instr_kind = instr_kind


class InstrAdd(object):
    """
    add x y z  // x = y + z
    """

    def __init__(self, x, y, z):
        self.instr_kind = Kind.add
        self.x = x
        self.y = y
        self.z = z


class InstrMove(object):
    """

    """

    def __init__(self, x, y, z):
        self.instr_kind = Kind.move
        self.x = x
        self.y = y
        self.z = z


class Quad(object):

    def __init__(self, op, result, x, y=''):
        self.type = op
        self.result = result
        self.x = x
        self.y = y


class QuadCondition(object):

    def __init__(self, op, condition, x='', y=''):
        self.type = op
        self.condition = condition
        self.x = x
        self.y = y


class QuadLabel(object):

    def __init__(self, op, label):
        self.type = op
        # self.condition = condition
        # self.body = body
        self.label = label


class QuadFunctionLabel(object):

    def __init__(self, op, func_name):
        self.type = op
        # self.condition = condition
        # self.body = body
        self.func_name = func_name


class QuadWhile(object):

    def __init__(self, op, condition, body, start):
        self.type = op
        self.condition = condition
        self.body = body
        self.start = start


class QuadDef(object):

    def __init__(self, op, args, body, func_name):
        self.type = op
        self.args = args
        self.body = body
        self.func_name = func_name
        # self.end = end


class QuadCall(object):

    def __init__(self, op, args, func_name):
        self.type = op
        self.args = args
        self.func_name = func_name


class QuadPrint(object):

    def __init__(self, op, value=''):
        self.type = op
        self.value = value


class InstrIf(object):

    def __init__(self):
        # 基本块
        self.kind = Kind.k_if
        # self.quads = []
        self.condition = []
        self.left = []
        self.right = []


class InstrPrint(object):

    def __init__(self):
        # 基本块
        self.kind = Kind.print
        # self.quads = []
        self.left = []


class InstrVar(object):

    def __init__(self):
        self.kind = Kind.var
        # self.quads = []
        self.left = []


class IR(object):

    def __init__(self):
        # 基本块
        self.instrs = []
