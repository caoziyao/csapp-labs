# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/20 
@desc:
"""
from src.commont.utils import is_space
from src.token import Token


def string_token(current_index, codes):
    """
    "abcdefg"
    :return: abcdefg
    """
    codes = codes[current_index:]

    i = 1
    l = len(codes)

    token = ''
    while i < l:
        c = codes[i]
        i += 1

        if c == '"':
            break
        else:
            token += c

    return i + current_index, token


def identify_keyword_token(current_index, codes):
    """
    var
    :return: var
    """
    codes = codes[current_index:]

    i = 0
    l = len(codes)

    token = ''
    while i < l:
        c = codes[i]
        i += 1

        if is_space(c):
            break
        else:
            token += c

    return i + current_index - 1, token


def next_token(current_index, codes):
    """
    :return:
    """
    codes = codes[current_index:]

    i = 0
    l = len(codes)

    token = ''
    while i < l:
        c = codes[i]
        i += 1

        if is_space(c):
            break

        if c.isalpha() or c == '_':
            # token += c
            i, token = identify_keyword_token(i - 1, codes)
        elif c.isdigit():
            # number
            token += c
        elif c == '"':
            # string
            i, token = string_token(i - 1, codes)
        elif c == '=':
            token = c

    if token.isdigit():
        token = int(token)

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

    print('token_list', token_list)


def lexer():
    # codes = """
    #     var a = "abc"
    #     if a = 3
    # """

    codes = 'var a = "abnd" '

    s = pase_list(codes)
