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


@unique
class InstrKind(Enum):
    const = 0
    move = 1
    add = 2


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
