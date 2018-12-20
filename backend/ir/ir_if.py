# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/12/20 
@desc:
"""

from common.utils import is_leaf
from common.expression import Type
from common.keywords import Keywords
from common.label_type import LabelType
from common.instr_kind import (
    QuadPrint, QuadLabel, QuadAssign, QuadCmpGoto, QuadGoto, QuadLessThen,
    QuadCall, QuadCondition, QuadFunctionLabel, QuadExpr, QuadFor
)
from backend.ir.base_ir import CommonVar
from backend.ir.ir_expression import IRExpression
from backend.ir.ir_assign import IRAssgin


class IRIf(object):

    def gen(self, node, quads):
        """
        if ( a ) {
            b
        } else {
            c
        }


        if a:
            goto t1
        c
        goto done
        t1:
            b

        done:
        :return:
        """
        from backend.ir.three_address import IRTree
        from backend.ir.ir_expression import IRExpression

        test_expr = node.test_expr
        if_stmt = node.if_stmt
        else_stmt = node.else_stmt


        # IRTree(quads).gen(init_stmt)

        tag_if = CommonVar().get_tmp_var()
        tag_done = CommonVar().get_tmp_var()

        # test_expr
        t1 = IRTree(quads).gen(test_expr)
        q1 = QuadCmpGoto(tag_if, condition=t1)
        quads.append(q1)

        # else_stmt
        IRTree(quads).gen(else_stmt)
        q2 = QuadGoto(tag_done, condition=None)
        quads.append(q2)

        # loop tag
        start = QuadLabel(LabelType.label, tag_if)
        quads.append(start)

        # body
        IRTree(quads).gen(if_stmt)

        # done
        end = QuadLabel(LabelType.label, tag_done)
        quads.append(end)

        # # condition
        # t2 = IRTree(quads).gen(test_expr)
        # q3 = QuadCmpGoto(tag_loop, condition=t2)
        # quads.append(q3)


