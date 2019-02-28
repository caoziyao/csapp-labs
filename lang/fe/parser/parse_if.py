# coding: utf-8

from lang.fe.experssion import ExprIf


def p_condition_if(p):
    'expression : IF LPAREN expression RPAREN L_BRACE expression R_BRACE ELSE L_BRACE expression R_BRACE'
    cond = p[3]
    if_code = p[6]
    else_code = p[10]
    p[0] = ExprIf(cond, if_code, else_code)


#
def p_condition_if_else(p):
    'expression : IF LPAREN expression RPAREN L_BRACE expression R_BRACE'
    cond = p[3]
    if_code = p[6]
    p[0] = ExprIf(cond, if_code)
