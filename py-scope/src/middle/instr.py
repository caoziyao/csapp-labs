# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/23 
@desc:
"""
from src.parser.expression import Kind


# 递归实现前序、中序、后序遍历
def pre_order(node):
    if node:
        print(node.value)
        pre_order(node.left)
        pre_order(node.right)


def mid_order(node):
    if node:
        pre_order(node.left)
        print(node.value)
        pre_order(node.right)


def gen_div(left, right):
    t = left / right
    return t


def gen_times(left, right):
    t = left * right
    return t


def gen_plus(left, right):
    t = left + right
    return t


def gen_minus(left, right):
    t = left - right
    return t


def gen_number(node):
    return node.value


def gen_assignment(left, right):
    t = '{} = {}'.format(str(left), str(right))
    return t


def gen_id(node):
    return node.value


def is_leaf(node):
    """

    :param node:
    :return:
    """
    if (node.left is None) and (node.right is None):
        return True
    else:
        return False


def post_order(node):
    root = {
        Kind.plus: gen_plus,
        Kind.minus: gen_minus,
        Kind.times: gen_times,
        Kind.div: gen_div,
        Kind.assignment: gen_assignment,
    }
    leaf = {
        Kind.number: gen_number,
        Kind.id: gen_id,
    }

    if node:
        left = post_order(node.left)
        right = post_order(node.right)

        kind = node.type
        if is_leaf(node):
            f = leaf[kind]
            t = f(node)
        else:
            f = root[kind]
            t = f(left, right)

        return t


def myinstr(ast):
    """

    :return:
    """
    t = post_order(ast)
    return t
