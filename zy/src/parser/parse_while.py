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
    ID, UNDEFIND, VAR, ExprVar, ExprCondition, ExprIsLessThen, ExprIsMoreThen, ExprWhile
)


# while (2 > 1) {a = 2}
def p_while(p):
    'statement : WHILE LPAREN expression RPAREN L_BRACE statement_list R_BRACE'
    condition = p[3]
    body = p[6]
    p[0] = ExprWhile(condition, body)


