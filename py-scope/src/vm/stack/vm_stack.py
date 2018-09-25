# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/26 
@desc:
"""
from src.common.expression import Kind
from src.common.utils import is_leaf

def process_ir(ir):
    kind = ir.kind
    if kind == Kind.k_if:
        pass


def vm(ir):
    instrs = ir.instrs

    for i in instrs:
        process_ir(ir)
