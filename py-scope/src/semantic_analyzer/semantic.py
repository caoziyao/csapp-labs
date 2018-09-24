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
from src.semantic_analyzer.sem_table import SemTable

table = SemTable()


def check_pus(node, left, right):
    left_type = left.type
    right_type = right.type
    if left_type != Kind.number:
        raise Exception('type mismatch {} != {}'.format(left_type, Kind.number))

    if right_type != Kind.number:
        raise Exception('type mismatch {} != {}'.format(right_type, Kind.number))

    return Kind.number


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

    return Kind.assignment


def check_var(node, left, right):
    name = left.value
    # t = {
    #     name: Kind.var
    # }
    table.enter(name, Kind.var)
    return table


def check_number(node):
    return node


def check_id(node):
    return node


def check_true(node):
    return node


def check_false(node):
    return node


def check_undefind(node):
    return node

def check_condition(node, left, right):
    # left_type = left.type
    # right_type = right.type
    # if left_type != Kind.number:
    #     raise Exception('type mismatch {} != {}'.format(left_type, Kind.number))
    #
    # if right_type != Kind.number:
    #     raise Exception('type mismatch {} != {}'.format(right_type, Kind.number))

    return Kind.k_if

def semantic(node):
    root = {
        Kind.plus: check_pus,
        # Kind.minus: check_minus,
        # Kind.times: check_times,
        # Kind.div: check_div,
        Kind.assignment: check_assignment,
        Kind.var: check_var,
        Kind.k_if: check_condition,
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
