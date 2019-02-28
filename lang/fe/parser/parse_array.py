# coding: utf-8

from lang.fe.experssion import (
    Number, ExprPlus, ExprMinus, ExprDiv, ExprTimes, ID, ExprArray, ExprArrayAccess)



def p_array_declar(p):
    'expression : l_square_bracket  r_square_bracket'
    name = ''
    p[0] = ExprArray(name)


def p_array_access(p):
    'expression : ID l_square_bracket NUMBER r_square_bracket'
    name = p[1]
    index = p[3]
    p[0] = ExprArrayAccess(name, index)
