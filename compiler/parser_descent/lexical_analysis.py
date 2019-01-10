# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/12/5 
@desc:
"""
from compiler.common.utils import is_space
from compiler.common.tokentype import Token, Type
from compiler.parser_descent.symbol_table import SysmbolTable
from compiler.common.keywords import Keywords


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


def number_token(current_index, codes):
    """
    12
    :return: 12
    """
    codes = codes[current_index:]

    i = 0
    l = len(codes)

    value = ''
    while i < l:
        c = codes[i]
        i += 1

        if c.isdigit():
            value += c
        else:
            break

    token = Token(Type.number, int(value))

    return i + current_index - 1, token


def identify_keyword_token(current_index, codes):
    """
    var
    :return: var
    """
    # global sysmbol_idx
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

    # m = ['var', 'if', 'while', 'for', 'print', 'else']
    m = Keywords.keywords()

    if value in m:
        token = Token(Type.keyword, value)
    else:
        token = Token(Type.id, value, 0)
        d = {
            'type': Type.id,
            'name': value
        }
        SysmbolTable[value] = d
        # sysmbol_idx += 1

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
        '=': Token(Type.assign, value),
        '>': Token(Type.more_then, value),
        '<': Token(Type.less_then, value),
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
        '{': Token(Type.braceLeft, value),
        '}': Token(Type.braceRight, value),
        '[': Token(Type.bracketLeft, value),
        ']': Token(Type.bracketRight, value),
    }

    token = m[value]

    return i + current_index, token


def semicolon_token(current_index, codes):
    """
    ;
    :param current_index:
    :param codes:
    :return:
    """
    value = codes[current_index]
    i = 1

    m = {
        ';': Token(Type.semicolon, value),
    }

    token = m[value]

    return i + current_index, token


def next_token(current_index, codes):
    """
    :return:
    """
    codes = codes[current_index:]

    c = codes[0]
    i = 1

    if c.isalpha() or c == '_':
        # token += c
        i, token = identify_keyword_token(i - 1, codes)
    elif c.isdigit():
        # number
        i, token = number_token(i - 1, codes)
    elif c == '"':
        # string
        i, token = string_token(i - 1, codes)
    elif c in '+-*/=><':
        i, token = operate_token(i - 1, codes)
    elif c in '(){}[]':
        i, token = parentheses_token(i - 1, codes)
    elif c == ';':
        i, token = semicolon_token(i - 1, codes)
    else:
        # error
        raise Exception('error next_token')

    # if value.isdigit():
    #     value = int(value)
    #     token = Token(Type.number, value)

    return i + current_index, token


def lexical_analysis(codes):
    """
    词法分析
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

    print(token_list)
    print('SysmbolTable', SysmbolTable)
    return token_list
