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
from src.common.expression import Kind

@unique
class InstrKind(Enum):
    const = 0
    move = 1
    plus = 2
    assignment = 3
    k_if = 4


class InstrT(object):

    def __init__(self, instr_kind):
        self.instr_kind = instr_kind


class InstrAdd(object):
    """
    add x y z  // x = y + z
    """

    def __init__(self, x, y, z):
        self.instr_kind = InstrKind.add
        self.x = x
        self.y = y
        self.z = z


class InstrMove(object):
    """

    """

    def __init__(self, x, y, z):
        self.instr_kind = InstrKind.move
        self.x = x
        self.y = y
        self.z = z


class Quad(object):

    def __init__(self, op, x, y='', result=''):
        self.op = op
        self.x = x
        self.y = y
        self.result = result


class InstrIf(object):

    def __init__(self):
        # 基本块
        self.kind = Kind.k_if
        # self.quads = []
        self.conditon = []
        self.left = []
        self.right = []

class InstrPrint(object):

    def __init__(self):
        # 基本块
        self.kind = Kind.print
        # self.quads = []
        self.left = []


class IR(object):

    def __init__(self):
        # 基本块
        self.instrs = []