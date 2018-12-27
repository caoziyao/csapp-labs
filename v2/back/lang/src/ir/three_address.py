# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/25 
@desc:
三地址码
"""
from lang.common import is_leaf
from lang.common import Kind
from compiler.common import (
    QuadPrint, QuadLabel, Quad, QuadWhile, QuadDef,
    QuadCall, QuadCondition, QuadFunctionLabel
)

index_tmp = 0


class IRTree(object):

    def __init__(self, root):
        self.root = root
        self.quads = []
        # self.index_tmp = index_tmp
        self.irfunc = {
            Kind.var: self.gen_instr_var,
            Kind.print: self.gen_instr_print,
            Kind.k_if: self.gen_instr_kif,
            Kind.kwhile: self.gen_instr_kwhile,
            Kind.kdef: self.gen_instr_def,
            Kind.call: self.gen_instr_call,
        }

    def get_tmp_var(self):
        global index_tmp

        t = '#{}'.format(index_tmp)
        index_tmp += 1
        return t

    def gen_expression(self, node):
        """
        表达式
        :param node:
        :return:
        """
        # m = {
        #     Kind.plus: self.gen_plus,
        #     Kind.times: self.gen_times,
        # }
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

    # def strip_string(self, str):
    #     """
    #     "abc" -> abc
    #     :param str:
    #     :return:
    #     todo
    #     """
    #     s = str.split('"', 1)[1].split('"')[0]
    #     return s

    def gen_instr_call(self, node):
        """

        :param node:
        :return:
        """
        args = node.args
        fname = node.func_name.value

        ra = []
        for arg in args:
            a = self.gen_expression(arg)
            ra.append(a)

        q = QuadCall(Kind.call, ra, fname)

        return q

    def gen_instr_def(self, node):
        """

        :param node:
        :return:
        """
        args = node.args
        body = node.body
        fname = node.func_name.value
        fname = 'func_{}'.format(fname)

        # fname:
        qfname = QuadFunctionLabel(Kind.kdef_name, fname)
        self.quads.append(qfname)

        # args
        ra = []
        for arg in args:
            a = self.gen_expression(arg)
            ra.append(a)

        # body
        rl = []
        for l in body:
            a = self.gen_instr(l)
            rl.append(a)

        # end
        # t2 = self.get_tmp_var()
        # end = QuadLabel(Kind.kdef_end, t2)

        q = QuadDef(Kind.kdef, ra, rl, fname)
        # self.quads.append(q)

        # self.quads.append(end)

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

        return q

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
        return q

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
        return q

    def gen_instr(self, node):
        """
        解析命令
        :param node:
        :return:
        """
        kind = node.type
        f = self.irfunc.get(kind, None)
        if f:
            r = f(node)
        else:
            raise Exception('not instr ir {}'.format(kind))

        return r

    def gen(self):

        r = self.gen_instr(self.root)
        if r:
            self.quads.append(r)

        return self.quads
