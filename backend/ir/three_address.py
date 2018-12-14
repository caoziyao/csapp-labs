# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/25 
@desc:
三地址码
"""
from common.utils import is_leaf
from common.expression import Type
from common.keywords import Keywords
from common.label_type import LabelType
from common.instr_kind import (
    QuadPrint, QuadLabel, QuadAssign, QuadWhile, QuadDef,
    QuadCall, QuadCondition, QuadFunctionLabel, QuadExpr, QuadFor
)


class IRTree(object):

    def __init__(self, root):
        self.root = root
        self.index = 0
        self.quads = []
        self.irfunc = {
            # Keywords.var: self.gen_instr_var,
            # Keywords.print: self.gen_instr_print,
            # Keywords.kif: self.gen_instr_kif,
            # Keywords.kwhile: self.gen_instr_kwhile,
            # Keywords.kdef: self.gen_instr_def,
            # Keywords.call: self.gen_instr_call,

            Type.keyword: self.gen_keyword,
            Type.assign: self.gen_instr_var,
        }

    def get_tmp_var(self):

        t = '#{}'.format(self.index)
        self.index += 1
        return t

    def strip_string(self, str):
        """
        "abc" -> abc
        :param str:
        :return:
        todo
        """
        s = str.split('"', 1)[1].split('"')[0]
        return s

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

        q = QuadCall(Keywords.call, ra, fname)

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
        qfname = QuadFunctionLabel(Keywords.kdef_name, fname)
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

        q = QuadDef(Keywords.kdef, ra, rl, fname)
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
        start = QuadLabel(Keywords.kwhile_start, t)
        self.quads.append(start)

        rc = self.gen_expression(cond)

        rl = []
        for l in body:
            a = self.gen_instr(l)
            rl.append(a)

        q = QuadWhile(Keywords.kwhile, rc, rl, start)

        return q

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
        # if node node:
        if is_leaf(node):
            # 叶子节点
            t = self.get_tmp_var()
            q = QuadAssign(t, node)
            self.quads.append(q)
            return t
        else:
            left = self.gen_expression(node.left)
            right = self.gen_expression(node.right)

            t = self.get_tmp_var()
            q = QuadExpr(node.type, t, left, right)
            self.quads.append(q)
            return t

    def gen_instr_for(self, node):
        """
        for () {
        }
        :param node:
        :return:
        """
        init_stmt = node.init_stmt
        update_stmt = node.update_stmt
        test_expr = node.test_expr

        self.gen_expression(init_stmt)

        t = self.get_tmp_var()
        start = QuadLabel(LabelType.forstart, t)
        self.quads.append(start)

        self.gen_expression(test_expr)
        self.gen_expression(update_stmt)

        t = self.get_tmp_var()
        end = QuadLabel(LabelType.forend, t)
        self.quads.append(end)

    def gen_keyword(self, node):
        """

        :return:
        """
        _type = node.type
        value = node.value

        d = {
            'for': self.gen_instr_for,
        }
        f = d.get(value, None)
        if f:
            r = f(node)
        else:
            raise Exception('not instr ir {}'.format(_type))

        return r

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
        q = QuadAssign(idf, res)
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

        q = QuadPrint(Keywords.print, res)
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

        q = QuadCondition(Keywords.kif, rc, rl, rr)
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
