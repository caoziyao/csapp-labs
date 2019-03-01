# coding: utf-8

import ply.lex as lex

# List of token names.   This is always required
tokens = (
    'COMMENT',  # 注释
    'NUMBER',  # number
    'PLUS',  # +
    'MINUS',  # -
    'TIMES',  # *
    'DIVIDE',  # /
    'EQUAL',  # =
    'DOUBLE_EQUAL',  # ==
    'LPAREN',  # (
    'RPAREN',  # )
    'ID',  # identify 字母数字下横线
    'STRING',  # string
    'L_BRACE',  # {
    'R_BRACE',  # {
    'IS_MORE_THEN',  # >
    'IS_LESS_THEN',  # <

    'l_square_bracket', # [
    'r_square_bracket', # ]
    'SEMICOLON',
    # 'IS_MORE_THEN_OR_EQUAL',      # >=
    # 'IS_LESS_THEN_OR_EQUAL',      # <=
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
# t_STRING = r'".*"'
t_STRING = r'"[ a-zA-Z_0-9\n\t]*"'
t_L_BRACE = r'\{'
t_R_BRACE = r'\}'
t_IS_MORE_THEN = r'\>'
t_IS_LESS_THEN = r'\<'
t_l_square_bracket = r'\['
t_r_square_bracket = r'\]'
t_SEMICOLON = r'\;'
# t_IS_MORE_THEN_OR_EQUAL = r'\>='
# t_IS_LESS_THEN_OR_EQUAL = r'\<='


keword = {
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'while': 'WHILE',
    'var': 'VAR',
    'true': 'TRUE',
    'false': 'FALSE',
    'print': 'PRINT',
    'def': 'DEF',
    'call': 'CALL',
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


# 注释
def t_COMMENT(t):
    r'\#.*'
    pass
    # r'\//.*'
    # No return value. Token discarded


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()
