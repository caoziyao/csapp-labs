# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/23
@desc:
三地址码
"""
from common.expression import Type
from common.keywords import Keywords


class BaseQuad(object):
    pass
    # def __init__(self, op, result, x, y=''):
    #     self.type = op
    #     self.result = result
    #     self.x = x
    #     self.y = y


class QuadExpr(object):

    def __init__(self, op, result, x, y):
        self.type = op
        self.result = result
        self.x = x
        self.y = y

    def __str__(self, level=0):
        ret = '{} {} {} {}'.format(self.result, self.x, self.type.name, self.y)
        # ret = "\t" * level + repr(self.type.name) + "\n"
        # ret += self.x
        # ret +=  self.y
        return ret


class QuadAssign(BaseQuad):

    def __init__(self, result, x):
        self.type = Type.assign
        self.result = result
        self.x = x
        # self.y = y

    def __str__(self, level=0):
        ret = '{} {} {}'.format(self.result, self.type.name, self.x)
        # ret = "\t" * level + repr(self.type.name) + "\n"
        # ret += self.x
        # ret +=  self.y
        return ret


class QuadLessThen(BaseQuad):

    def __init__(self, result, x):
        self.type = Type.less_then
        self.left = result
        self.right = x
        # self.y = y

    def __str__(self, level=0):
        ret = '{} {} {}'.format(self.left, self.type.name, self.right)
        # ret = "\t" * level + repr(self.type.name) + "\n"
        # ret += self.x
        # ret +=  self.y
        return ret

class QuadGoto(BaseQuad):

    def __init__(self, label):
        self.type = Type.goto
        self.label = label
        # self.right = x
        # self.y = y

    def __str__(self, level=0):
        ret = '{} {} '.format(self.type.name, self.label)
        # ret = "\t" * level + repr(self.type.name) + "\n"
        # ret += self.x
        # ret +=  self.y
        return ret



class QuadFor(BaseQuad):

    def __init__(self, init_stmt=None, test_expr=None, update_stmt=None, code=None):
        self.type = Keywords.kfor
        self.init_stmt = init_stmt
        self.test_expr = test_expr
        self.update_stmt = update_stmt
        self.code = code


class QuadCondition(BaseQuad):

    def __init__(self, op, condition, x='', y=''):
        self.type = op
        self.condition = condition
        self.x = x
        self.y = y


class QuadLabel(BaseQuad):

    def __init__(self, op, label):
        self.type = op
        # self.condition = condition
        # self.body = body
        self.label = label

    def __str__(self, level=0):
        ret = 'tag:{} {}'.format(self.type.name, self.label)
        return ret


class QuadFunctionLabel(BaseQuad):

    def __init__(self, op, func_name):
        self.type = op
        # self.condition = condition
        # self.body = body
        self.func_name = func_name


class QuadWhile(BaseQuad):

    def __init__(self, op, condition, body, start):
        self.type = op
        self.condition = condition
        self.body = body
        self.start = start


class QuadDef(BaseQuad):

    def __init__(self, op, args, body, func_name):
        self.type = op
        self.args = args
        self.body = body
        self.func_name = func_name
        # self.end = end


class QuadCall(BaseQuad):

    def __init__(self, op, args, func_name):
        self.type = op
        self.args = args
        self.func_name = func_name


class QuadPrint(BaseQuad):

    def __init__(self, op, value=''):
        self.type = op
        self.value = value
#
#
# class InstrIf(object):
#
#     def __init__(self):
#         # 基本块
#         self.kind = Kind.k_if
#         # self.quads = []
#         self.condition = []
#         self.left = []
#         self.right = []
#
#
# class InstrPrint(object):
#
#     def __init__(self):
#         # 基本块
#         self.kind = Kind.print
#         # self.quads = []
#         self.left = []
#
#
# class InstrVar(object):
#
#     def __init__(self):
#         self.kind = Kind.var
#         # self.quads = []
#         self.left = []
#
#
# class IR(object):
#
#     def __init__(self):
#         # 基本块
#         self.instrs = []

#
# class InstrT(object):
#
#     def __init__(self, instr_kind):
#         self.instr_kind = instr_kind
#
#
# class InstrAdd(object):
#     """
#     add x y z  // x = y + z
#     """
#
#     def __init__(self, x, y, z):
#         self.instr_kind = Type.add
#         self.x = x
#         self.y = y
#         self.z = z
#
#
# class InstrMove(object):
#     """
#
#     """
#
#     def __init__(self, x, y, z):
#         self.instr_kind = Kind.move
#         self.x = x
#         self.y = y
#         self.z = z
