# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/23 
@desc:
"""
from src.lexer.lexer import tokens
from src.common.expression import (
    ExprPrint, PRINT, STRING, ID, Number
)


# _instruction


# def p_print(p):
#     'instruction : print expression'
#     p[0] = ExprPrint(p[1], p[2])
#
#
# def p_print_print(p):
#     'print : PRINT'
#     p[0] = PRINT(p[1])

#
# def p_print_value(p):
#     'value : STRING'
#     p[0] = STRING(p[1])
#
#
# def p_print_id(p):
#     'value : ID'
#     p[0] = ID(p[1])
#
#
# def p_print_number(p):
#     'value : NUMBER'
#     p[0] = Number(p[1])


##################

def p_print(p):
    'expression : print value'
    p[0] = ExprPrint(p[1], p[2])


def p_print_print(p):
    'print : PRINT'
    p[0] = PRINT(p[1])


def p_print_value(p):
    'value : STRING'
    p[0] = STRING(p[1])


def p_print_id(p):
    'value : ID'
    p[0] = ID(p[1])


def p_print_number(p):
    'value : NUMBER'
    p[0] = Number(p[1])