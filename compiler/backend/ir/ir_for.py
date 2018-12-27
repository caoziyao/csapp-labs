# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/12/13 
@desc:
"""
from compiler.common.label_type import LabelType
from compiler.common.instr_kind import (
    QuadLabel, QuadCmpGoto, QuadGoto
)
from compiler.backend.ir.base_ir import CommonVar


class IRFor(object):

    def gen_instr_for(self, node, quads):
        """
        for (a; b; c) {
            d
        }

        a
        if b:
            goto loop
        goto done

        loop:
            d;
            c;

            if b:
                goto loop

        done
        :param node:
        :return:
        """
        from compiler.backend.ir import IRTree

        init_stmt = node.init_stmt
        update_stmt = node.update_stmt
        test_expr = node.test_expr
        body = node.code

        IRTree(quads).gen(init_stmt)


        tag_loop = CommonVar().get_tmp_var()
        tag_done = CommonVar().get_tmp_var()

        # condition
        t1 = IRTree(quads).gen(test_expr)
        q1 = QuadCmpGoto(tag_loop, condition=t1)
        quads.append(q1)

        q2 = QuadGoto(tag_done, condition=None)
        quads.append(q2)

        # loop tag
        start = QuadLabel(LabelType.label, tag_loop)
        quads.append(start)

        # body
        IRTree(quads).gen(body)
        IRTree(quads).gen(update_stmt)

        # condition
        t2 = IRTree(quads).gen(test_expr)
        q3 = QuadCmpGoto(tag_loop, condition=t2)
        quads.append(q3)

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
