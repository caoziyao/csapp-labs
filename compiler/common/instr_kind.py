# coding: utf-8
"""
三地址码

x = y op z
x = op z
x = y
goto L
if x goto L
if x relop y goto L

param x1
param x2
...
param xn
call p, n
y = call p, n

x = y[i]
x[i] = y

x = &y
x = *y
*x = y

"""
from compiler.common.expression import Type
from compiler.common.keywords import Keywords


class BaseQuad(object):

    def __init__(self, op=None, result=None, arg1=None, arg2=None):
        self.op = op
        self.result = result
        self.arg1 = arg1
        self.arg2 = arg2


class QuadExpr(object):

    def __init__(self, op, result, x, y):
        self.op = op
        self.result = result
        self.x = x
        self.y = y

    def __str__(self, level=0):
        ret = '{} {} {} {}'.format(self.result, self.x, self.op.name, self.y)
        return ret


class QuadAssign(BaseQuad):

    def __init__(self, arg1=None, arg2=None):
        super(QuadAssign, self).__init__()
        self.op = Type.assign
        self.arg1 = arg1
        self.arg2 = arg2

    def __str__(self, level=0):
        ret = '{} {} {}'.format(self.arg1, self.op.name, self.arg2)
        return ret


class QuadLessThen(BaseQuad):

    def __init__(self, arg1=None, arg2=None):
        super(QuadLessThen, self).__init__()
        self.op = Type.less_then
        self.arg1 = arg1
        self.arg2 = arg2

    def __str__(self, level=0):
        ret = '{} {} {}'.format(self.arg1, self.op.name, self.arg2)
        return ret


class QuadGoto(BaseQuad):

    def __init__(self, label, condition=None):
        self.op = Type.goto
        self.label = label
        self.condition = condition

    def __str__(self, level=0):
        ret = '{} {} '.format(self.op.name, self.label)
        return ret


class QuadCmpGoto(BaseQuad):

    def __init__(self, label, condition=None):
        self.op = Type.cmdgoto
        self.label = label
        self.condition = condition

    def __str__(self, level=0):
        ret = '{} {} '.format(self.op.name, self.label)
        return ret


class QuadCondition(BaseQuad):

    def __init__(self, op, condition, x='', y=''):
        self.op = op
        self.condition = condition
        self.x = x
        self.y = y


class QuadFor(BaseQuad):

    def __init__(self, init_stmt=None, test_expr=None, update_stmt=None, code=None):
        self.op = Keywords.kfor
        self.init_stmt = init_stmt
        self.test_expr = test_expr
        self.update_stmt = update_stmt
        self.code = code


class QuadLabel(BaseQuad):

    def __init__(self, op, label):
        self.op = op
        self.label = label

    def __str__(self, level=0):
        ret = 'tag:{} {}'.format(self.op.name, self.label)
        return ret


class QuadFunctionLabel(BaseQuad):

    def __init__(self, op, func_name):
        self.op = op
        self.func_name = func_name


class QuadWhile(BaseQuad):

    def __init__(self, op, condition, body, start):
        self.op = op
        self.condition = condition
        self.body = body
        self.start = start


class QuadDef(BaseQuad):

    def __init__(self, op, args, body, func_name):
        self.op = op
        self.args = args
        self.body = body
        self.func_name = func_name


class QuadCall(BaseQuad):

    def __init__(self, op, args, func_name):
        self.op = op
        self.args = args
        self.func_name = func_name


class QuadPrint(BaseQuad):

    def __init__(self, op, value=''):
        self.op = op
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
