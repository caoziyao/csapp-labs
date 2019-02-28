# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2019/2/28 
@desc:
"""
from .quads import Quads
from .common import is_leaf
from .quad_assign import QuadAssign
from .quad_expr import QuadExpr


class IRExpression(object):

    def gen_expression(self, node, quads):
        """
        表达式
        :param node:
        :return:
        """
        if is_leaf(node):
            # 叶子节点
            t = Quads().tmp_var()
            q = QuadAssign(arg1=t, arg2=node)
            quads.append(q)
            return t
        else:
            left = self.gen_expression(node.left, quads)
            right = self.gen_expression(node.right, quads)

            t = Quads().tmp_var()
            q = QuadExpr(node.type, t, left, right)
            quads.append(q)
            return t
