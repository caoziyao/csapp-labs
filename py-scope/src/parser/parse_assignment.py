# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/23 
@desc:
"""

from src.parser.expression import (
    ExprAssignment, ID, Number
)
from src.lexer.lexer import tokens


def p_assignment(p):
    'expression : id EQUAL value'
    p[0] = ExprAssignment(p[1], p[3])
    # pass


def p_assignment_id(p):
    'id : ID'
    p[0] = ID(p[1])


def p_assignment_value(p):
    'value : NUMBER'
    p[0] = Number(p[1])
