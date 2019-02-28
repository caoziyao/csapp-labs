# coding: utf-8

from lang.fe.experssion import (
    Number, ExprPlus, ExprMinus, ExprDiv, ExprTimes, ID, ExprIf, ExprArrayDeclar, ExprArrayAccess)


def p_array_declar(p):
    'array : ID EQUAL l_square_bracket  r_square_bracket'
    name = p[1]
    p[0] = ExprArrayDeclar(name)


def p_array_access(p):
    'array : ID l_square_bracket NUMBER r_square_bracket'
    name = p[1]
    index = p[3]
    p[0] = ExprArrayAccess(name, index)
