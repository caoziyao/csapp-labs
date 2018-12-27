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

from compiler.common.tokentype import Type


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
        return ret


class String(object):
    def __init__(self, value):
        self.type = Type.string
        self.value = value

    def __str__(self, level=0):
        ret = "\t" * level + repr(self.value) + "\n"
        return ret

#############################

class Node(object):

    def __str__(self, level=0):
        ret = "\t" * level + repr(self.type.name) + "\n"
        ret += self.left.__str__(level + 1)
        ret += self.right.__str__(level + 1)
        return ret


class ExpAssgin(Node):
    """
    =
    """

    def __init__(self, left, right):
        self.type = Type.assign
        self.left = left  # class Exp
        self.right = right  # class Exp


class ExpLessThen(Node):
    """
    <
    """

    def __init__(self, left, right):
        self.type = Type.less_then
        self.left = left  # class Exp
        self.right = right  # class Exp


class ExpMoreThen(Node):
    """
    >
    """

    def __init__(self, left, right):
        self.type = Type.more_then
        self.left = left  # class Exp
        self.right = right  # class Exp


class ExpAdd(Node):
    """
    +
    """

    def __init__(self, left, right):
        self.type = Type.add
        self.left = left  # class Exp
        self.right = right  # class Exp


class ExpTimes(Node):
    """
    *
    """

    def __init__(self, left, right):
        self.type = Type.times
        self.left = left  # class Exp
        self.right = right  # class Exp


class ExpDiv(Node):
    """
    /
    """

    def __init__(self, left, right):
        self.type = Type.div
        self.left = left  # class Exp
        self.right = right  # class Exp


class ExpSub(Node):
    """
    -
    """

    def __init__(self, left, right):
        self.type = Type.sub
        self.left = left  # class Exp
        self.right = right  # class Exp


class ExpFor(Node):
    """
    for (initializationStatement; testExpression; updateStatement) {
           // codes
    }
    """

    def __init__(self, init_stmt=None, test_expr=None, update_stmt=None, code=None):
        self.type = Type.keyword
        self.value = 'for'
        self.init_stmt = init_stmt
        self.test_expr = test_expr
        self.update_stmt = update_stmt
        self.code = code

    def __str__(self, level=0):
        ret = "\t" * level + repr(self.value) + "\n"
        ret += 'init_stmt' + self.init_stmt.__str__(level + 1)
        ret += 'test_expr' + self.test_expr.__str__(level + 1)
        ret += 'update_stmt' + self.update_stmt.__str__(level + 1)
        ret += 'code' + self.code.__str__(level + 1)
        return ret


class ExpIf(Node):
    """
    if (testExpression) {
        // statement(s) inside the body of if
    }
    else {
        // statement(s) inside the body of else
    }
    """

    def __init__(self, test_expr=None, if_stmt=None, else_stmt=None):
        self.type = Type.keyword
        self.value = 'if'
        self.test_expr = test_expr
        self.if_stmt = if_stmt
        self.else_stmt = else_stmt

    def __str__(self, level=0):
        ret = "\t" * level + repr(self.value) + "\n"
        ret += 'test_expr' + self.test_expr.__str__(level + 1)
        ret += 'if_stmt' + self.if_stmt.__str__(level + 1)
        ret += 'else_stmt' + self.else_stmt.__str__(level + 1)
        return ret

# class ExprCondition(Node):
#     """
#     if
#     """
#
#     def __init__(self, condition, left, right):
#         self.type = Kind.k_if
#         self.condition = condition
#         self.left = left  # class Exp
#         self.right = right  # class Exp
#
#     def __str__(self, level=0):
#         ret = "\t" * level + repr(self.type.name) + "\n"
#         ret += self.condition.__str__(level + 1)
#         ret += self.left.__str__(level + 1)
#         ret += self.right.__str__(level + 1)
#         return ret
#
#
# class ExprWhile(Node):
#     """ while """
#
#     def __init__(self, condition, body):
#         self.type = Kind.kwhile
#         self.condition = condition
#         self.body = body  # class Exp
#
#     def __str__(self, level=0):
#         ret = "\t" * level + repr(self.type.name) + "\n"
#         ret += self.condition.__str__(level + 1)
#         ret += self.body.__str__(level + 1)
#         return ret
