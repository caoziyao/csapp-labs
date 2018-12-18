# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/12/13 
@desc:
"""
from common.utils import is_leaf
from common.expression import Type
from common.keywords import Keywords
from common.label_type import LabelType
from common.instr_kind import (
    QuadPrint, QuadLabel, QuadAssign, QuadWhile, QuadDef,
    QuadCall, QuadCondition, QuadFunctionLabel, QuadExpr, QuadFor
)
from backend.ir.base_ir import CommonVar
from backend.ir.ir_expression import IRExpression

class IRFor(object):

    def gen_instr_for(self, node, quads):
        """
        for () {
        }
        :param node:
        :return:
        """
        init_stmt = node.init_stmt
        update_stmt = node.update_stmt
        test_expr = node.test_expr

        exp = IRExpression()
        exp.gen_expression(init_stmt, quads)

        t = CommonVar().get_tmp_var()
        start = QuadLabel(LabelType.forstart, t)
        quads.append(start)

        exp.gen_expression(test_expr, quads)
        exp.gen_expression(update_stmt, quads)

        t = CommonVar().get_tmp_var()
        end = QuadLabel(LabelType.forend, t)
        quads.append(end)