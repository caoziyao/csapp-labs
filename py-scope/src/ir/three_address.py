# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/25 
@desc:
"""

from src.common.expression import Kind
from src.ir.instr_kind import Quad, IR, InstrIf, InstrPrint, InstrVar

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


def gen_is_more_then(node, left, right):
    name = left.value


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
        quad = Quad(Kind.plus, left.value, right.value)
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
        l = []
        x = gen_expression(right)
        # l.extend(x)
        # l.extend()


    elif kind == Kind.plus:
        x = gen_expression(node)

    elif kind == Kind.print:
        x = gen_print(node, left, right)
    else:
        x = []

    return x


def gen_var(node, left, right):
    quad = Quad(Kind.var, left.value, right.value)
    return quad


def gen_print(node, left, right):
    quads = []
    quad = Quad(Kind.print, right.value)
    quads.append(quad)
    return quads


def three_address(node):
    kind = node.type
    left = node.left
    right = node.right

    if kind == Kind.k_if:
        instr = InstrIf()
        condition = node.condition
        r = gen_expression(condition)
        instr.condition.extend(r)

        l = gen_slist(left)
        instr.left.extend(l)
        r = gen_slist(right)
        instr.right.extend(r)

    elif kind == Kind.print:
        instr = InstrPrint()
        r = gen_print(node, left, right)
        instr.left.extend(r)

    elif kind == Kind.var:
        instr = InstrVar()
        q = gen_var(node, left, right)
        instr.left.append(q)
        # instr
    else:
        raise Exception('not kind')

    ir.instrs.append(instr)

    return ir