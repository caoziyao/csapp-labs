# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/28 
@desc:
"""

from zy.src.lexer.lexer import tokens
from zy.src.common.expression import (
    ExprPrint, PRINT, STRING, ID, Number
)


def p_print(p):
    'statement : print expression'
    p[0] = ExprPrint(p[1], p[2])


def p_print_print(p):
    'print : PRINT'
    p[0] = PRINT(p[1])


def p_print_value(p):
    'expression : STRING'
    p[0] = STRING(p[1])
