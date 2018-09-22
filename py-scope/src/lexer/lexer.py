# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/23 
@desc:
"""

import ply.lex as lex

# List of token names.   This is always required
tokens = (
    'NUMBER',           # number
    'PLUS',             # +
    'MINUS',            # -
    'TIMES',            # *
    'DIVIDE',           # /
    'EQUAL',            # =
    'DOUBLE_EQUAL',     # ==
    'LPAREN',           # (
    'RPAREN',           # )
    'ID',               # identify 字母数字下横线
)

# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EQUAL = r'='
t_DOUBLE_EQUAL = r'=='


keword = {
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'while': 'WHILE',
    'var': 'VAR',
    'true': 'TRUE',
    'false': 'FALSE',
}

tokens = list(tokens) + list(keword.values())


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = keword.get(t.value, 'ID')  # Check for reserved words
    return t


# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()
