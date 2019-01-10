# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/12/19 
@desc:
"""

from compiler.common.instr_kind import (
    QuadLessThen
)
from compiler.backend.ir.ir_expression import IRExpression

class IRLessThen(object):


    def gen(self, node, quads):
        """
        var a = 123
        :param node:
        :return:
        """
        # idf = node.left
        expr = node.right

        e = IRExpression()
        res = e.gen_expression(expr, quads)

        # t = self.get_tmp_var()
        q = QuadLessThen(arg1=node.left, arg2=res)

        quads.append(q)

        return q