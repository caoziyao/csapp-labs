# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/24 
@desc:
"""
from src.common.expression import Kind
from src.common.utils import is_leaf
from src.semantic.sem_table import SemTable
from src.ir import three_address

table = SemTable()


def check_pus(node, left, right):
    left_type = left.type
    right_type = right.type
    if left_type != Kind.number:
        raise Exception('type mismatch {} != {}'.format(left_type, Kind.number))

    if right_type != Kind.number:
        raise Exception('type mismatch {} != {}'.format(right_type, Kind.number))

    return node


def check_assignment(node, left, right):
    left_type = left.type
    right_type = right.type
    left_value = left.value

    if not table.lookup(left.value):
        raise Exception('{} is not defined'.format(left_value))

    if left_type != Kind.id:
        raise Exception('type mismatch {} != {}'.format(left_type, Kind.id))

    if right_type != Kind.number:
        raise Exception('type mismatch {} != {}'.format(right_type, Kind.number))

    return node


def check_var(node, left, right):
    name = left.value
    # t = {
    #     name: Kind.var
    # }
    table.enter(name, Kind.var)
    return table


def check_condition(node, left, right):
    # left_type = left.type
    # right_type = right.type
    # if left_type != Kind.number:
    #     raise Exception('type mismatch {} != {}'.format(left_type, Kind.number))
    #
    # if right_type != Kind.number:
    #     raise Exception('type mismatch {} != {}'.format(right_type, Kind.number))

    return Kind.k_if


def check_print(node, left, right):
    return node


def semantic(node):
    root = {
        Kind.plus: check_pus,
        # Kind.minus: check_minus,
        # Kind.times: check_times,
        # Kind.div: check_div,
        Kind.assignment: check_assignment,
        Kind.var: check_var,
        Kind.k_if: check_condition,
        Kind.print: check_print,
    }
    leaf = {
        # Kind.number: check_number,
        # Kind.id: check_id,
        # Kind.true: check_true,
        # Kind.false: check_false,
        # Kind.undefind: check_undefind,
    }

    if node:
        left = semantic(node.left)
        right = semantic(node.right)

        kind = node.type
        if is_leaf(node):
            return node
            # f = leaf[kind]
            # t = f(node)
        else:
            f = root[kind]
            t = f(node, left, right)

        return t


def semantic_analyzer(node):
    """

    :param node:
    :return:
    """
    # res = semantic(node)
    ir = three_address(node)

    return ir
