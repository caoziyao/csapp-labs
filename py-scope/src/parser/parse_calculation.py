# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/23 
@desc:
"""
from src.parser.expression import Number, ExprPlus, ExprMinus, ExprDiv, ExprTimes
# Get the token map from the lexer.  This is required.
from src.lexer.lexer import tokens


def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = ExprPlus(p[1], p[3])


def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = ExprMinus(p[1], p[3])


def p_expression_term(p):
    'expression : term'
    p[0] = p[1]


def p_term_times(p):
    'term : term TIMES factor'
    # p[0] = p[1] * p[3]
    p[0] = ExprTimes(p[1], p[3])


def p_term_div(p):
    'term : term DIVIDE factor'
    p[0] = ExprDiv(p[1], p[3])


def p_term_factor(p):
    'term : factor'
    p[0] = p[1]


def p_factor_num(p):
    """factor : NUMBER
    """
    # p[0] = p[1]
    p[0] = Number(p[1])


def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!", p)
    # raise SyntaxError
