# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/28 
@desc:
"""

from src.lexer.lexer import tokens
from src.common.expression import (
    ID, UNDEFIND, VAR, ExprVar, ExprCondition, ExprIsLessThen, ExprIsMoreThen
)


def p_statement_list_1(p):
    'statement_list : statement'
    p[0] = [p[1]]


def p_statement_list_2(p):
    'statement_list : statement_list statement'
    p[0] = p[1] + [p[2]]