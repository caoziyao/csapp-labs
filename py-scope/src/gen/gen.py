# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/23 
@desc:
"""
from src.common.expression import Kind
from src.gen.section import Section
from src.common.utils import is_leaf


def gen_print(node, left, right):
    # t = node.value
    # print('gen_print {}'.format(t))
    return node


def gen_id(node):
    t = node.value
    print('gen_id {}'.format(t))
    return node


def gen_string(node):
    t = node.value
    print('gen_string {}'.format(t))
    return node


def gen_code(node, section):
    """
    section .data
    :return:
    """
    root = {
        Kind.id: gen_id,
        Kind.string: gen_string,
        Kind.print: gen_print,
    }

    if node:
        left = gen_code(node.left, section)
        right = gen_code(node.right, section)

        kind = node.type
        if is_leaf(node):
            return node
            # f = leaf[kind]
            # t = f(node)
        else:
            f = root[kind]
            t = f(node, left, right)

        return t


def gen(ast):
    """

    :return:
    """
    section = Section()
    # t = post_order(ast)
    gen_code(ast, section)

    section.gen()
