# coding: utf-8


from lang.base.kind import Kind
from .quad_label import QuadLabel
from .quad_func import QuadFunc
from .ir_expression import IRExpression


class IRTree(object):

    def __init__(self):
        self.index = 0
        self.irfunc = {

            Kind.kdef: self.gen_func,
            Kind.var: self.gen_expression,
            # Kind.keyword: self.gen_keyword,
            # Kind.assign: self.gen_instr_var,
            # Kind.less_then: self.gen_less_then,
        }

    def gen_func(self, node):
        """

        :param node:
        :return:
        """
        args = node.args
        body = node.body
        fname = node.func_name.value
        fname = 'func_{}'.format(fname)

        # fname:
        # qfname = QuadLabel(Kind.kdef_name, fname)
        # self.quads.append(qfname)

        # args
        # ra = []
        # for arg in args:
        #     a = self.gen_expression(arg)
        #     ra.append(a)

        # body
        # rl = []
        # for l in body:
        #     a = self.gen_expression(l)
        #     rl.append(a)

        ir_args = []
        ir_body = self.gen_expression(body)

        # end
        # t2 = self.get_tmp_var()
        # end = QuadLabel(Kind.kdef_end, t2)

        q = QuadFunc(Kind.kdef, ir_args, ir_body, fname)

        qs = [q, ]
        return qs

    def gen_expression(self, node):
        """

        :return:
        """

        ir = IRExpression()

        qs = []
        ir.gen_expression(node, qs)

        return qs

    def gen_three(self, node):
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
    #
    # def gen(self, root):
    #     """
    #     :return:
    #     """
    #     r = self.gen_instr(root)
    #
    #     return r
