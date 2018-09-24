# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/24 
@desc:
"""

from src.lexer.lexer import tokens
from src.common.expression import (
    ExprAssignment, ID, UNDEFIND, VAR, ExprVar, ExprCondition, ExprIsLessThen, ExprIsMoreThen
)


# if (2 > 1) {a = 2} else {a = 1}
def p_condition_if(p):
    'expression : IF LPAREN expression RPAREN L_BRACE expression R_BRACE ELSE L_BRACE expression R_BRACE'
    conditon = p[3]
    yes = p[6]
    no = p[10]
    p[0] = ExprCondition(conditon, yes, no)


def p_condition_conf(p):
    """
    expression : expression IS_MORE_THEN expression
               | expression IS_LESS_THEN expression
    """
    if p[2] == '>':
        p[0] = ExprIsMoreThen(p[1], p[3])
    elif p[2] == '<':
        p[0] = ExprIsLessThen(p[1], p[3])

# def p_assignment(p):
#     'expression : id EQUAL expression'
#     p[0] = ExprAssignment(p[1], p[3])
#
#
# def p_assignment_id(p):
#     'id : ID'
#     p[0] = ID(p[1])
