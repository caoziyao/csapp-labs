# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/20
@desc:
"""
from parser_descent.src.commont.utils import is_space
from parser_descent.src.token import Token, Type


def string_token(current_index, codes):
    """
    "abcdefg"
    :return: abcdefg
    """
    codes = codes[current_index:]

    i = 1
    l = len(codes)

    value = ''
    while i < l:
        c = codes[i]
        i += 1

        if c == '"':
            break
        else:
            value += c

    token = Token(Type.string, value)

    return i + current_index, token


def identify_keyword_token(current_index, codes):
    """
    var
    :return: var
    """
    codes = codes[current_index:]

    i = 0
    l = len(codes)

    value = ''
    while i < l:
        c = codes[i]
        i += 1

        if is_space(c):
            break
        else:
            value += c

    m = ['var', 'if', 'while']

    if value in m:
        token = Token(Type.keyword, value)
    else:
        token = Token(Type.identifier, value)

    return i + current_index - 1, token


def operate_token(current_index, codes):
    """
    + - * /
    :param current_index:
    :param codes:
    :return:
    """
    value = codes[current_index]
    i = 1

    m = {
        '+': Token(Type.add, value),
        '-': Token(Type.sub, value),
        '*': Token(Type.times, value),
        '/': Token(Type.div, value),
        '=': Token(Type.equal, value),
    }

    token = m[value]

    return i + current_index, token

def parentheses_token(current_index, codes):
    """
    ()
    :param current_index:
    :param codes:
    :return:
    """
    value = codes[current_index]
    i = 1

    m = {
        '(': Token(Type.parenthesesLeft, value),
        ')': Token(Type.parenthesesRight, value),
    }

    token = m[value]

    return i + current_index, token


def next_token(current_index, codes):
    """
    :return:
    """
    codes = codes[current_index:]

    i = 0
    value = ''
    c = codes[i]
    i += 1

    if c.isalpha() or c == '_':
        # token += c
        i, token = identify_keyword_token(i - 1, codes)
    elif c.isdigit():
        # number
        value += c
    elif c == '"':
        # string
        i, token = string_token(i - 1, codes)
    elif c in '+-*/=':
        i, token = operate_token(i - 1, codes)
        # token = Token(Type.equal, '=')
    elif c in '()':
        i, token = parentheses_token(i - 1, codes)
        # break
    else:
        pass
        # error
        # raise Exception('error next_token')

    if value.isdigit():
        value = int(value)
        token = Token(Type.number, value)

    return i + current_index, token


def pase_list(codes):
    """
    :param codes:
    :return:
    """
    i = 0
    l = len(codes)

    token_list = []
    while i < l:
        c = codes[i]
        i += 1

        if is_space(c):
            continue

        i, token = next_token(i - 1, codes)

        token_list.append(token)

    return token_list


def lexer(codes):
    # codes = """
    #     var a = "abc"
    #     if a = 3
    # # """

    # codes = 'var a = "abnd" '

    s = pase_list(codes)

    print('token_list', s)
    return s
