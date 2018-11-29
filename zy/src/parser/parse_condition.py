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
    ID, UNDEFIND, VAR, ExprVar, ExprCondition, ExprIsLessThen, ExprIsMoreThen
)


# if (2 > 1) {a = 2} else {a = 1}
def p_condition_if(p):
    'statement : IF LPAREN expression RPAREN L_BRACE statement_list R_BRACE ELSE L_BRACE statement_list R_BRACE'
    condition = p[3]
    yes = p[6]
    no = p[10]
    p[0] = ExprCondition(condition, yes, no)


def p_condition_conf(p):
    """
    expression : expression IS_MORE_THEN expression
               | expression IS_LESS_THEN expression
    """
    if p[2] == '>':
        p[0] = ExprIsMoreThen(p[1], p[3])
    elif p[2] == '<':
        p[0] = ExprIsLessThen(p[1], p[3])

