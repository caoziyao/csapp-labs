# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/12/19 
@desc:
"""

from common.utils import is_leaf
from common.expression import Type
from common.keywords import Keywords
from common.label_type import LabelType
from common.instr_kind import (
    QuadPrint, QuadLabel, QuadAssign, QuadWhile, QuadDef, QuadLessThen,
    QuadCall, QuadCondition, QuadFunctionLabel, QuadExpr, QuadFor
)
from backend.ir.base_ir import CommonVar
from backend.ir.ir_expression import IRExpression

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
        q = QuadLessThen(node.left, res)

        quads.append(q)

        return res