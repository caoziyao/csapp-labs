# coding: utf-8

from enum import Enum, unique

"""
1. 定义 tao 语言的语法细节，并挑选一个合适的形式描述出来。
2. 编写一个 Compiler-compiler，它能编译 tao 语言的定义，并生成某种数据结构。
3. 编写一个 Parser，它通过解释 Compiler-compiler 生成的数据结构，将 Token 序列编译成 Syntax Tree。
"""

class BinaryOperator(Enum):

    plus = 1        # +
    minus = 2       # -
    multiply = 3    # *
    divide = 4      # /



class Expression(object):

    def __init__(self):
        pass



class NumberExpression(Expression):
    """数字表达式"""
    def __init__(self):
        super(NumberExpression, self).__init__()
        # value 是数字
        self.value = None


class BinaryExpression(Expression):
    """二元运算表达式"""
    def __init__(self):
        super(BinaryExpression, self).__init__()
        self.first = None
        self.second = None
        self.op = None

    def binary_expression(self, op, left, right):
        pass


class VarExpression(Expression):
    """赋值表达式"""
    def __init__(self, node):
        super(VarExpression, self).__init__()
        self.first = None
        self.second = None
        self.op = None
        self.var = None
        self.is_leaf = True
        self.node = node

    def binary_expression(self, op, left, right):
        pass