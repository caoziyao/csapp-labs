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

from parser_descent.tokentype import Type


# 数据结构
# @unique
# class Kind(Enum):
#     int = 0
#     add = 1
#     times = 2
#     sub = 3
#     div = 4
#
#
# class Exp(object):
#
#     def __init__(self, kind):
#         self.type = kind  # enum Kind


class Number(object):

    def __init__(self, value):
        self.type = Type.number
        self.value = value

    def __str__(self, level=0):
        ret = "\t" * level + repr(self.value) + "\n"
        # for child in self.children:
        return ret

    # def __repr__(self):
    #     return '<tree node representation>'


class ID(object):
    def __init__(self, value):
        self.type = Type.id
        self.value = value

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


class ExpAssgin(Node):

    def __init__(self, left, right):
        self.type = Type.assign
        self.left = left  # class Exp
        self.right = right  # class Exp


class ExpAdd(Node):

    def __init__(self, left, right):
        self.type = Type.add
        self.left = left  # class Exp
        self.right = right  # class Exp


class ExpTimes(Node):

    def __init__(self, left, right):
        self.type = Type.times
        self.left = left  # class Exp
        self.right = right  # class Exp


class ExpDiv(Node):

    def __init__(self, left, right):
        self.type = Type.div
        self.left = left  # class Exp
        self.right = right  # class Exp


class ExpSub(Node):

    def __init__(self, left, right):
        self.type = Type.sub
        self.left = left  # class Exp
        self.right = right  # class Exp
