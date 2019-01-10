# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/28 
@desc:
"""

from lang.common import (
    ID, ExprCall, ExprDef
)


def p_def(p):
    'statement : DEF func_name LPAREN  RPAREN L_BRACE statement_list R_BRACE'
    args = []
    func_name = p[2]
    body = p[6]

    p[0] = ExprDef(func_name, args, body)


def p_def_arg(p):
    'statement : DEF func_name LPAREN ID RPAREN L_BRACE statement_list R_BRACE'
    func_name = p[2]
    args = [ID(p[4])]
    body = p[7]
    p[0] = ExprDef(func_name, args, body)


def p_def_funcname(p):
    'func_name : ID'
    p[0] = ID(p[1])


def p_call(p):
    'statement : CALL func_name LPAREN RPAREN'
    func_name = p[2]
    args = []
    p[0] = ExprCall(func_name, args)

# def p_def_args(p):
#     'print : ID'
#     p[0] = PRINT(p[1])

#
# def p_print_value(p):
#     'expression : STRING'
#     p[0] = STRING(p[1])
