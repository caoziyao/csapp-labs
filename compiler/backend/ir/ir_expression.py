# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/12/14 
@desc:
"""
from compiler.common.utils import is_leaf
from compiler.common.instr_kind import (
    QuadAssign, QuadExpr
)
from compiler.backend.ir.base_ir import CommonVar

class IRExpression(object):

    def gen_expression(self, node, quads):
        """
        表达式
        :param node:
        :return:
        """
        # if node node:
        if is_leaf(node):
            # 叶子节点
            # t = self.get_tmp_var()
            t = CommonVar().get_tmp_var()
            q = QuadAssign(arg1=t, arg2=node)
            # self.quads.append(q)
            quads.append(q)
            return t
        else:
            left = self.gen_expression(node.left, quads)
            right = self.gen_expression(node.right, quads)

            # t = self.get_tmp_var()
            t = CommonVar().get_tmp_var()
            q = QuadExpr(node.type, t, left, right)
            # self.quads.append(q)
            quads.append(q)
            return t

