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
    ID, UNDEFIND, VAR, ExprVar
)
# precedence = (
#     ('left', 'PLUS', 'MINUS'),
#     ('left', 'TIMES', 'DIVIDE'),
# )

def p_assignment_var(p):
    'expression : VAR ID'
    p[0] = ExprVar(ID(p[2]), UNDEFIND())


def p_assignment_var_equal(p):
    'expression : VAR ID EQUAL expression'
    p[0] = ExprVar(ID(p[2]), p[4])



# def p_assignment(p):
#     'expression : id EQUAL value'
#     p[0] = ExprAssignment(p[1], p[3])

#
# def p_assignment_id(p):
#     'value : expression'
#     p[0] = ID(p[1])



# def p_assignment_var(p):
#     'expression : VAR ID'
#     p[0] = ExprVar(ID(p[2]), UNDEFIND())
#
#
# def p_assignment_var_equal(p):
#     'expression : VAR ID EQUAL expression'
#     p[0] = ExprVar(ID(p[2]), p[4])
#
#
# def p_assignment(p):
#     'expression : id EQUAL expression'
#     p[0] = ExprAssignment(p[1], p[3])
#
#
# def p_assignment_id(p):
#     'id : ID'
#     p[0] = ID(p[1])
