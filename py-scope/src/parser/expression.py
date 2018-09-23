# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/22
@desc:
"""

from enum import Enum, unique


# 数据结构
@unique
class Kind(Enum):
    number = 0  # 0-9
    plus = 1    # +
    times = 2
    minus = 3
    div = 4
    operator = 5  # 操作符 +-*/
    assignment = 6  # 赋值
    id = 7  # id
    var = 8 # var
    string = 9  # string
    print = 10  # print


class Number(object):

    def __init__(self, value):
        self.type = Kind.number  # enum Kind
        self.value = value
        self.left = None
        self.right = None

    def __str__(self, level=0):
        ret = "\t" * level + repr(self.value) + "\n"
        # for child in self.children:
        return ret


class ID(object):

    def __init__(self, value):
        self.type = Kind.id  # enum Kind
        self.value = value
        self.left = None
        self.right = None

    def __str__(self, level=0):
        ret = "\t" * level + repr(self.value) + "\n"
        # for child in self.children:
        return ret


class VAR(object):

    def __init__(self, value):
        self.type = Kind.var  # enum Kind
        self.value = value
        self.left = None
        self.right = None

    def __str__(self, level=0):
        ret = "\t" * level + repr(self.value) + "\n"
        # for child in self.children:
        return ret

class STRING(object):

    def __init__(self, value):
        self.type = Kind.string  # enum Kind
        self.value = value
        self.left = None
        self.right = None

    def __str__(self, level=0):
        ret = "\t" * level + repr(self.value) + "\n"
        # for child in self.children:
        return ret

class PRINT(object):

    def __init__(self, value):
        self.type = Kind.print  # enum Kind
        self.value = value
        self.left = None
        self.right = None

    def __str__(self, level=0):
        ret = "\t" * level + repr(self.value) + "\n"
        # for child in self.children:
        return ret

class Node(object):

    def __str__(self, level=0):
        ret = "\t" * level + repr(self.type.name) + "\n"
        ret += self.left.__str__(level + 1)
        ret += self.right.__str__(level + 1)
        return ret


class BinOp(Node):

    def __init__(self, left, right):
        self.type = Kind.operator  # enum Kind
        self.left = left  # class Exp
        self.right = right  # class Exp


class ExprPlus(Node):

    def __init__(self, left, right):
        self.type = Kind.plus
        self.left = left  # class Exp
        self.right = right  # class Exp


class ExprMinus(Node):

    def __init__(self, left, right):
        self.type = Kind.minus
        self.left = left  # class Exp
        self.right = right  # class Exp


class ExprTimes(Node):

    def __init__(self, left, right):
        self.type = Kind.times
        self.left = left  # class Exp
        self.right = right  # class Exp


class ExprDiv(Node):

    def __init__(self, left, right):
        self.type = Kind.div
        self.left = left  # class Exp
        self.right = right  # class Exp


class ExprAssignment(Node):

    def __init__(self, left, right):
        self.type = Kind.assignment
        self.left = left  # class Exp
        self.right = right  # class Exp


class ExprPrint(Node):

    def __init__(self, left, right):
        self.type = Kind.print
        self.left = left  # class Exp
        self.right = right  # class Exp