# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/21 
@desc:
抽象语法树数据结构]
优美打印
"""

from enum import Enum, unique


# 数据结构
@unique
class Kind(Enum):
    int = 0
    add = 1
    times = 2
    sub = 3
    div = 4


class Exp(object):

    def __init__(self, kind):
        self.kind = kind  # enum Kind


class ExpInt(object):

    def __init__(self, kind, n):
        self.kind = kind  # enum Kind
        self.n = n

    def __str__(self, level=0):
        ret = "\t" * level + repr(self.n) + "\n"
        # for child in self.children:
        return ret

    # def __repr__(self):
    #     return '<tree node representation>'


class Node(object):

    def __str__(self, level=0):
        ret = "\t" * level + repr(self.kind.name) + "\n"
        ret += self.exp_left.__str__(level + 1)
        ret += self.exp_right.__str__(level + 1)
        return ret


class ExpAdd(Node):

    def __init__(self, kind, exp_left, exp_right):
        self.kind = kind  # enum Kind
        self.exp_left = exp_left  # class Exp
        self.exp_right = exp_right  # class Exp


class ExpTimes(Node):

    def __init__(self, kind, exp_left, exp_right):
        self.kind = kind  # enum Kind
        self.exp_left = exp_left  # class Exp
        self.exp_right = exp_right  # class Exp


class ExpDiv(Node):

    def __init__(self, kind, exp_left, exp_right):
        self.kind = kind  # enum Kind
        self.exp_left = exp_left  # class Exp
        self.exp_right = exp_right  # class Exp

