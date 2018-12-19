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
    QuadPrint, QuadLabel, QuadAssign, QuadWhile, QuadGoto, QuadLessThen,
    QuadCall, QuadCondition, QuadFunctionLabel, QuadExpr, QuadFor
)
from backend.ir.base_ir import CommonVar
from backend.ir.ir_expression import IRExpression
from backend.ir.ir_assign import IRAssgin


class IRFor(object):

    def gen_instr_for(self, node, quads):
        """
        for (a; b; c) {
            d
        }

        a
        if b:
            goto done

        start:
            d;
            c;

            if b:
                goto start

        done
        :param node:
        :return:
        """
        from backend.ir.three_address import IRTree
        from backend.ir.ir_expression import IRExpression

        init_stmt = node.init_stmt
        update_stmt = node.update_stmt
        test_expr = node.test_expr
        body = node.code

        IRTree(quads).gen(init_stmt)

        # condition
        tag_done = CommonVar().get_tmp_var()
        t1 = IRTree(quads).gen(test_expr)
        q1 = QuadGoto(tag_done, condition=t1)
        quads.append(q1)

        # loop tag
        tag_loop = CommonVar().get_tmp_var()
        start = QuadLabel(LabelType.label, tag_loop)
        quads.append(start)

        # body
        IRTree(quads).gen(body)
        IRTree(quads).gen(update_stmt)

        # condition
        t2 = IRTree(quads).gen(test_expr)
        q2 = QuadGoto(tag_loop, condition=t2)
        quads.append(q2)

        # done
        end = QuadLabel(LabelType.label, tag_done)
        quads.append(end)

        # exp = IRExpression()
        # # exp.gen_expression(init_stmt, quads)
        #
        # IRAssgin().gen_assgin(init_stmt, quads)
        #
        #
        # t = CommonVar().get_tmp_var()
        # start = QuadLabel(LabelType.forloop, t)
        # quads.append(start)
        #
        # exp.gen_expression(test_expr, quads)
        # # exp.gen_expression(update_stmt, quads)
        # IRAssgin().gen_assgin(update_stmt, quads)
        #
        # t = CommonVar().get_tmp_var()
        # end = QuadLabel(LabelType.fordone, t)
        # quads.append(end)
