# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/12/13 
@desc:
"""
from compiler.common.instr_kind import (
    QuadAssign
)
from compiler.backend.ir.ir_expression import IRExpression

class IRAssgin(object):


    def gen_assgin(self, node, quads):
        """
        var a = 123
        :param node:
        :return:
        """
        idf = node.left
        expr = node.right

        e = IRExpression()
        res = e.gen_expression(expr, quads)

        # t = self.get_tmp_var()
        q = QuadAssign(arg1=idf, arg2=res)

        quads.append(q)
        # return q
