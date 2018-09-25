# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/25 
@desc:
"""

from src.common.expression import Kind
from src.common.utils import is_leaf
from src.ir.instr_kind import Quad, IR, InstrIf, InstrPrint

ir = IR()


def gen_pus(node, left, right):
    # left_type = left.type
    # right_type = right.type

    x1 = left + right
    # print('x = x1')
    return x1


def gen_assignment(node, left, right):
    # left_type = left.type
    # right_type = right.type
    # left_value = left.value

    # x1 = left.value + right.value
    print('{} = {}'.format(left, right))

    return right


def gen_var(node, left, right):
    name = left.value
    # t = {
    #     name: Kind.var
    # }


def gen_is_more_then(node, left, right):
    name = left.value


def gen_print(node, left, right):
    return node


def gen_number(node):
    return node.value


def gen_id(node):
    return node.value


def gen_condition(node, left, right):
    cond = node.condition
    x = three_address(cond)
    print('Cjmp(x, L1, L2)')
    print('Label L1:')

    return Kind.k_if


def gen_expression(node):
    """
    表达式
    :return:
    """
    kind = node.type
    left = node.left
    right = node.right

    quads = []
    if kind == Kind.is_more_then:
        quad = Quad(Kind.is_more_then, left.value, right.value)
        quads.append(quad)

    elif kind == Kind.number:
        quad = Quad(Kind.number, node.value)
        quads.append(quad)

    elif kind == Kind.plus:
        quad = Quad(Kind.number, left.value, right.value)
        quads.append(quad)

    elif kind == Kind.string:
        quad = Quad(Kind.string, node.value)
        quads.append(quad)

    return quads


def gen_slist(node):
    kind = node.type
    left = node.left
    right = node.right

    # block = Block()
    if kind == Kind.assignment:
        x = gen_expression(right)


    elif kind == Kind.plus:
        x = gen_expression(node)

    else:
        x = []

    return x


def three_address(node):
    kind = node.type
    left = node.left
    right = node.right

    if kind == Kind.k_if:
        instr = InstrIf()
        condition = node.condition
        r = gen_expression(condition)
        instr.conditon.extend(r)

        l = gen_slist(left)
        instr.left.extend(l)
        r = gen_slist(right)
        instr.right.extend(r)

    elif kind == Kind.print:
        instr = InstrPrint()
        r = gen_expression(right)
        instr.left.extend(r)
    else:
        raise Exception('not kind')

    ir.instrs.append(instr)

    return ir
    # root = {
    #     Kind.plus: gen_pus,
    #     # Kind.minus: gen_minus,
    #     # Kind.times: gen_times,
    #     # Kind.div: gen_div,
    #     Kind.assignment: gen_assignment,
    #     Kind.var: gen_var,
    #     Kind.k_if: gen_condition,
    #     Kind.print: gen_print,
    #     Kind.is_more_then: gen_is_more_then,
    # }
    # leaf = {
    #     Kind.number: gen_number,
    #     Kind.id: gen_id,
    #     # Kind.true: gen_true,
    #     # Kind.false: gen_false,
    #     # Kind.undefind: gen_undefind,
    # }
    #
    # if node:
    #     left = three_address(node.left)
    #     right = three_address(node.right)
    #
    #     kind = node.type
    #     if is_leaf(node):
    #         # return node
    #         f = leaf[kind]
    #         t = f(node)
    #     else:
    #         f = root[kind]
    #         t = f(node, left, right)
    #
    #     return t
