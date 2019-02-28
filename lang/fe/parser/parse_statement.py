# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/28 
@desc:
"""

from lang.fe.experssion import (
    ID, UNDEFIND, ExprVar
)
#
#
def p_statement_assign(p):
    'statement : ID EQUAL expression'
    # names[p[1]] = p[3]
    p[0] = ExprVar(ID(p[1]), p[3])
#
#
# def p_statement_var_assign(p):
#     'statement : VAR ID EQUAL expression'
#     # names[p[1]] = p[3]
#     p[0] = ExprVar(ID(p[2]), p[4])
#
#
# def p_statement_var_undefind(p):
#     'statement : VAR ID'
#     # names[p[1]] = p[3]
#     p[0] = ExprVar(ID(p[2]), UNDEFIND())

# def p_statement_expr(p):
#     'statement : expression'
#     print(p[1])
#
#
# def p_statement_list_1(p):
#     'statement_list : statement'
#     p[0] = [p[1]]
#
#
# def p_statement_list_2(p):
#     'statement_list : statement_list statement'
#     p[0] = p[1] + [p[2]]
