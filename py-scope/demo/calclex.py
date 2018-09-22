# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/21 
@desc:
"""

# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
import ply.lex as lex

# List of token names.   This is always required
# 标记列表
tokens = (
    'NUMBER',
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
)

# Regular expression rules for simple tokens
# 标记的规则
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


# A regular expression rule with some action code
# 标记的规则
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


# Define a rule so we can track line numbers
# 行号和位置信息
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
# 忽略字符
t_ignore = ' \t'


# Error handling rule
# 错误处理
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)  # 跳过一个字符。


# Build the lexer
# 构建和使用lexer
lexer = lex.lex()


def atest1():
    # Test it out
    data = '''
    if 3 + 4 * 10
      + -20 *2
    '''

    # Give the lexer some input
    lexer.input(data)

    # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)


def atest2():
    data = '''
        var a = 12  # var 注释
    '''

    # Give the lexer some input
    lexer.input(data)

    # Tokenize
    while True:
        # 返回下一个LexToken类型的标记实例
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)


def main():
    atest2()


if __name__ == '__main__':
    main()
