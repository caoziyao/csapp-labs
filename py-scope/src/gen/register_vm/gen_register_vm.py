# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/26 
@desc:
"""
from src.common.expression import Kind

codes = []

rn = 0
labeln = 0


def get_register():
    global rn
    rn += 1
    return 'r{}'.format(rn)


def get_label():
    global labeln
    labeln += 1
    return 'L{}'.format(labeln)


def gen_slist(nodes):
    for node in nodes:
        kind = node.op
        if kind == Kind.number:
            r = get_register()
            codes.append('mov {} {}'.format(r, node.x))
        elif kind == Kind.print:
            codes.append('print {}'.format(node.x))

    # elif kind == Kind.number:


def gen_k_if(inst):
    """"""
    # cond = inst.condition[0]
    for cond in inst.condition:
        if cond.op == Kind.is_more_then:
            r1 = get_register()
            r2 = get_register()
            r3 = get_register()
            codes.append('mov {} {}'.format(r1, cond.x))
            codes.append('mov {} {}'.format(r2, cond.y))
            codes.append('comp {} {} {}'.format(r1, r2, r3))
        else:
            # todo
            pass

        l1 = get_label()
        l2 = get_label()
        l3 = get_label()
        codes.append('cjmp {} {} {}'.format(r3, l1, l2))

        codes.append('{}:'.format(l1))
        gen_slist(inst.left)
        codes.append('{}:'.format(l2))
        gen_slist(inst.right)
        codes.append('{}:'.format(l3))


def gen_var(inst):
    """

    :param inst:
    :return:
    """
    code = inst.left
    # op = code.op

    for item in code:
        r1 = get_register()
        codes.append('mov {} {}'.format(r1, item.y))


def gen_register_vm(ir):
    instrs = ir.instrs

    global codes
    codes = []
    for inst in instrs:
        if inst.kind == Kind.k_if:
            gen_k_if(inst)

        elif inst.kind == Kind.var:
            gen_var(inst)

    return codes
