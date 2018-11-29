# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/28 
@desc:
"""

from zy.src.common.expression import (
    Number, ExprPlus, ExprMinus, ExprDiv, ExprTimes, TRUE, FALSE,
    ID, UNDEFIND, VAR, ExprVar,
)
# from src.lexer.lexer import tokens

# Parsing rules

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'UMINUS'),
)




def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    if p[2] == '+':
        p[0] = ExprPlus(p[1], p[3])
    elif p[2] == '-':
        p[0] = ExprMinus(p[1], p[3])
    elif p[2] == '*':
        p[0] = ExprTimes(p[1], p[3])
    elif p[2] == '/':
        p[0] = ExprDiv(p[1], p[3])


def p_expression_uminus(p):
    "expression : '-' expression %prec UMINUS"
    p[0] = -p[2]


def p_expression_group(p):
    "expression : LPAREN expression RPAREN"
    p[0] = p[2]


def p_expression_number(p):
    "expression : NUMBER"
    p[0] = Number(p[1])


def p_expression_name(p):
    "expression : ID"
    p[0] = ID(p[1])


def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")
