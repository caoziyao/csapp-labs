# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/25 
@desc:
"""
from src.common.utils import is_leaf
from src.common.expression import Kind
from src.ir.instr_kind import QuadPrint, QuadLabel, Quad, QuadWhile, InstrIf, InstrPrint, InstrVar, QuadCondition

#
# ir = IR()
#
#
# def gen_pus(node, left, right):
#     # quads = []
#     quad = Quad(Kind.plus, left, right)
#     # quads.append(quad)
#
#     return quad
#
#
# def gen_minus(node, left, right):
#     quad = Quad(Kind.minus, left, right)
#
#     return quad
#
#
# def gen_times(node, left, right):
#     quad = Quad(Kind.times, left, right)
#
#     return quad
#
#
# def gen_div(node, left, right):
#     pass
#
#
# def gen_number(node):
#     pass
#
#
# def gen_id(node):
#     pass
#
#
# def gen_expression(node):
#     expre_list = []
#
#     gen_expression_tree(node, expre_list)
#
#     return expre_list
#
#
# def gen_expression_tree(node, expre_list):
#     """
#     表达式
#     :return:
#     """
#     root = {
#         Kind.plus: gen_pus,
#         Kind.minus: gen_minus,
#         Kind.times: gen_times,
#         Kind.div: gen_div,
#         # Kind.minus: check_minus,
#         # Kind.times: check_times,
#         # Kind.div: check_div,
#     }
#     leaf = {
#         Kind.number: gen_number,
#         Kind.id: gen_id,
#         # Kind.true: check_true,
#         # Kind.false: check_false,
#         # Kind.undefind: check_undefind,
#     }
#
#     if node:
#         left = gen_expression_tree(node.left, expre_list)
#         right = gen_expression_tree(node.right, expre_list)
#
#         kind = node.type
#         if is_leaf(node):
#             # quads.append(node)
#             return node
#             # f = leaf[kind]
#             # t = f(node)
#         else:
#             f = root[kind]
#             t = f(node, left, right)
#             expre_list.append(t)
#
#             return t
#     return expre_list
#     # kind = node.type
#     # left = node.left
#     # right = node.right
#     #
#     # quads = []
#     # if kind == Kind.is_more_then:
#     #     quad = Quad(Kind.is_more_then, left, right)
#     #     quads.append(quad)
#     #
#     # elif kind == Kind.number:
#     #     quad = Quad(Kind.number, node)
#     #     quads.append(quad)
#     #
#     # elif kind == Kind.plus:
#     #     quad = Quad(Kind.plus, left, right)
#     #     quads.append(quad)
#     #
#     # elif kind == Kind.string:
#     #     quad = Quad(Kind.string, node)
#     #     quads.append(quad)
#     #
#     # return quads
#
#
# def gen_slist(node):
#     kind = node.type
#     left = node.left
#     right = node.right
#
#     # block = Block()
#     if kind == Kind.assignment:
#         l = []
#         x = gen_expression(right)
#         # l.extend(x)
#         # l.extend()
#
#
#     elif kind == Kind.plus:
#         x = gen_expression(node)
#
#     elif kind == Kind.print:
#         x = gen_print(node, left, right)
#     else:
#         x = []
#
#     return x
#
#
# def gen_var(node, left, right):
#     qs = gen_expression(right)
#
#     quad = Quad(Kind.var, left, qs)
#
#     return quad
#
#
# def gen_print(node, left, right):
#     quads = []
#     quad = Quad(Kind.print, right)
#     quads.append(quad)
#     return quads
#
#
# def three_address(node):
#     kind = node.type
#     left = node.left
#     right = node.right
#     global ir
#     ir = IR()
#
#     if kind == Kind.k_if:
#         instr = InstrIf()
#         condition = node.condition
#         r = gen_expression(condition)
#         instr.condition.extend(r)
#
#         l = gen_slist(left)
#         instr.left.extend(l)
#         r = gen_slist(right)
#         instr.right.extend(r)
#
#     elif kind == Kind.print:
#         instr = InstrPrint()
#         r = gen_print(node, left, right)
#         instr.left.extend(r)
#
#     elif kind == Kind.var:
#         instr = InstrVar()
#         q = gen_var(node, left, right)
#         instr.left.append(q)
#         # instr
#     else:
#         raise Exception('not kind')
#
#     ir.instrs.append(instr)
#
#     return ir


index_tmp = 0


class IRTree(object):

    def __init__(self, root):
        self.root = root
        self.quads = []
        # self.index_tmp = index_tmp

    def get_tmp_var(self):
        global index_tmp

        t = '#{}'.format(index_tmp)
        index_tmp += 1
        return t

    def gen_plus(self, node):
        """
        1 + 2
        :param node:
        :return:
        """
        pass

    def gen_times(self, node):
        """
        1 * 2
        :param node:
        :return:
        """
        pass

    def gen_expression(self, node):
        """
        表达式
        :param node:
        :return:
        """
        m = {
            Kind.plus: self.gen_plus,
            Kind.times: self.gen_times,
        }
        if node:
            left = self.gen_expression(node.left)
            right = self.gen_expression(node.right)

            if is_leaf(node):
                # 叶子节点
                t = self.get_tmp_var()
                q = Quad(node.type, t, node)
                self.quads.append(q)
                return t
            else:
                kind = node.type
                t = self.get_tmp_var()
                q = Quad(node.type, t, left, right)
                self.quads.append(q)
                return t

    def gen_instr_var(self, node):
        """
        var a = 123
        :param node:
        :return:
        """
        idf = node.left
        expr = node.right

        res = self.gen_expression(expr)

        # t = self.get_tmp_var()
        q = Quad(Kind.var, idf, res)

        # self.quads.append(q)
        return q

    def gen_instr_print(self, node):
        """
        var a = 123
        :param node:
        :return:
        """
        left = node.left
        expr = node.right

        res = self.gen_expression(expr)

        q = QuadPrint(Kind.print, res)

        # self.quads.append(q)
        return q

    def gen_instr(self, node):
        """
        解析命令
        :param node:
        :return:
        """
        kind = node.type
        m = {
            Kind.var: self.gen_instr_var,
            Kind.print: self.gen_instr_print,
            Kind.k_if: self.gen_instr_kif,
            Kind.kwhile: self.gen_instr_kwhile,
        }

        f = m.get(kind, None)
        if f:
            r = f(node)
        else:
            raise Exception('not instr ir {}'.format(kind))

        return r

    def gen_instr_kif(self, node):
        """
        :param node:
        :return:
        """
        cond = node.condition
        left = node.left
        right = node.right

        rc = self.gen_expression(cond)

        rl = []
        for l in left:
            a = self.gen_instr(l)
            rl.append(a)

        rr = []
        for r in right:
            b = self.gen_instr(r)
            rr.append(b)

        q = QuadCondition(Kind.k_if, rc, rl, rr)

        # self.quads.append(q)
        return q

    def gen_instr_kwhile(self, node):
        """
        while (1) {}
        :param node:
        :return:
        """
        cond = node.condition
        body = node.body

        t = self.get_tmp_var()
        start = QuadLabel(Kind.kwhile_start, t)
        self.quads.append(start)

        rc = self.gen_expression(cond)

        rl = []
        for l in body:
            a = self.gen_instr(l)
            rl.append(a)

        q = QuadWhile(Kind.kwhile, rc, rl, start)

        # self.quads.append(q)
        return q

    def gen(self):

        kind = self.root.type

        m = {
            Kind.var: self.gen_instr_var,
            Kind.print: self.gen_instr_print,
            Kind.k_if: self.gen_instr_kif,
            Kind.kwhile: self.gen_instr_kwhile,
        }

        f = m.get(kind, None)
        if f:
            r = f(self.root)
            self.quads.append(r)
        else:
            raise Exception('not ir {}'.format(kind))

        return self.quads
