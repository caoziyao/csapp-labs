# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/28 
@desc:
"""

from lang.fe.experssion import (
    Number, ExprPlus, ExprMinus, ExprDiv, ExprTimes, ID, ExprVar, ExprArray)

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'UMINUS'),
)


def p_statement_expr(p):
    "expression : expression SEMICOLON"
    p[0] = p[1]


# def p_statement_list_1(p):
#     'expression_list : expression '
#     p[0] = [p[1]]


def p_statement_list_2(p):
    'expression : expression expression'
    l = []
    if isinstance(p[1], list):
        l.extend(p[1])
    else:
        l.append(p[1])

    if isinstance(p[2], list):
        l.extend(p[2])
    else:
        l.append(p[2])

    p[0] = l


def p_statement_assign(p):
    'expression : ID EQUAL expression'
    p[0] = ExprVar(ID(p[1]), p[3])


def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression

    '''
    if p[2] == '+':
        p[0] = ExprPlus(p[1], p[3])
    elif p[2] == '-':
        p[0] = ExprMinus(p[1], p[3])
    elif p[2] == '*':
        p[0] = ExprTimes(p[1], p[3])
    elif p[2] == '/':
        p[0] = ExprDiv(p[1], p[3])
    # elif p[2] == '=':
    #     p[0] = ExprVar(p[1], p[3])


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
    print("Syntax error at EOF", p)
