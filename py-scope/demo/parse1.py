# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/21 
@desc:
"""
from ply.lex import lex
from ply.yacc import yacc

# Token list
tokens = [
    'NUM',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'EQUAL',
    'ALPHA',
    'ID',
    'COMMENT',
]
# Ignored characters
t_ignore = ' \t\n'
# Token specifications (as regexs)
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

reserved = {
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'while': 'WHILE',
    'var': 'VAR',
}

tokens = list(tokens) + list(reserved.values())


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t


def t_EQUAL(t):
    r'='
    return t


def t_ALPHA(t):
    r'[a-zA-Z]'
    return t


# 注释
def t_COMMENT(t):
    r'\#.*'
    pass
    # No return value. Token discarded


# Token processing functions
def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t


# Error handler
def t_error(t):
    print('Bad character: {!r}'.format(t.value[0]))
    t.skip(1)


# Build the lexer
lexer = lex()


# Grammar rules and handler functions
def p_expr(p):
    '''
    expr : expr PLUS term
        | expr MINUS term
    '''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]


def p_expr_term(p):
    '''
    expr : term
    '''
    p[0] = p[1]


def p_term(p):
    '''
    term : term TIMES factor
    | term DIVIDE factor
    '''
    if p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]


def p_term_factor(p):
    '''
    term : factor
    '''
    p[0] = p[1]


def p_factor(p):
    '''
    factor : NUM
    '''
    p[0] = p[1]


def p_factor_group(p):
    '''
    factor : LPAREN expr RPAREN
    '''
    p[0] = p[2]


def p_error(p):
    print('Syntax error')


def atest2():
    parser = yacc()

    print(parser.parse('2'))
    print(parser.parse('2+(3+4)*5'))


def main():
    atest2()


if __name__ == '__main__':
    main()
