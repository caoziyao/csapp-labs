# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/21 
@desc:
递归下降分析算法

每个非终结符一个分析函数
用 前看符号 指导生成式规则的选择
"""
from parser_descent.tokentype import Type
from parser_descent.expression import ExpInt, ExpAdd, ExpTimes, Kind, ExpDiv

current_index = 0


def current_token(tokens):
    """
    :param current_index:
    :param tokens:
    :return:
    """
    global current_index
    t = tokens[current_index]
    current_index += 1

    return t


def next_index():
    global current_index
    current_index += 1


def back_index():
    global current_index
    current_index -= 1


def parse_expr(tokens):
    """
    expr -> term + term
        -> term - term
    :return:
    """
    root = parse_term(tokens)

    t = current_token(tokens)

    while t.type in [Type.add, Type.sub]:
        if t.type == Type.add:
            right = parse_term(tokens)
            # val += right
            left = root
            root = ExpAdd(Kind.add, left, right)
        elif t.type == Type.sub:
            right = parse_term(tokens)
            # val -= right
            left = root
            root = ExpAdd(Kind.sub, left, right)

        if current_index >= len(tokens):
            break

        t = current_token(tokens)

    # else:
    #     raise Exception('parse_expr')

    return root


def parse_term(tokens):
    """
    term -> factor * factor
        | factor / factor
    :return:
    """
    root = parse_factor(tokens)

    # while current_index < len(tokens):
    if current_index >= len(tokens):
        return root

    t = current_token(tokens)

    if t.type not in [Type.times, Type.div]:
        back_index()
        return root

    while t.type in [Type.times, Type.div]:
        if t.type == Type.times:
            right = parse_factor(tokens)
            left = root
            root = ExpTimes(Kind.times, left, right)
            # val *= right
        elif t.type == Type.div:
            right = parse_factor(tokens)
            # val /= right
            left = root
            root = ExpDiv(Kind.div, left, right)

        if current_index >= len(tokens):
            break

        t = current_token(tokens)

    back_index()
    return root


# def parse_new_expr(tokens):
#     """
#
#     :param tokens:
#     :return:
#     """
#     parse_new_expr(tokens)

def parse_factor(tokens):
    """
    factor -> num
        -> expr
    :return:
    """
    t = current_token(tokens)
    _type = t.type
    if _type == Type.number:
        # return t.value
        return ExpInt(Kind.int, t.value)
    # elif _type == Type.parenthesesLeft:
    #     # back_index()
    #     root = parse_expr(tokens)
    #     return root
    # elif _type == Type.parenthesesRight:
    #     return None
    else:
        raise Exception('expect number but {}'.format(t.value))


def parse(tokens):
    """

    :return:
    """
    val = parse_expr(tokens)
    print(val)
    return val


def parse_number(token):
    """
    number
    :return:
    """
    # t = current_token(tokens)
    value = token.value
    if isinstance(value, int):
        return
    else:
        raise Exception('expect number but {}'.format(str(value)))


def parse_operate(token):
    """
    +-*/
    :return:
    """
    # t = current_token(tokens)
    value = token.value
    if value in '+-*/':
        return
    else:
        raise Exception('expect +-*/ but {}'.format(str(value)))
