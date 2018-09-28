# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/26 
@desc:
"""
from src.common.expression import Kind
from src.ir.instr_kind import Quad

#
# codes = []
#
# rn = 0
# labeln = 0
#
# stack = []
#
#
# def get_register():
#     global rn
#     rn += 1
#     return 'r{}'.format(rn)
#
#
# def get_label():
#     global labeln
#     labeln += 1
#     return 'L{}'.format(labeln)
#
#
# def gen_slist(nodes):
#     for node in nodes:
#         kind = node.op
#         if kind == Kind.number:
#             r = get_register()
#             codes.append('mov {} {}'.format(r, node.x.value))
#         elif kind == Kind.print:
#             codes.append('print {}'.format(node.x.value))
#
#     # elif kind == Kind.number:
#
#
# def gen_k_if(inst):
#     """"""
#     # cond = inst.condition[0]
#     for cond in inst.condition:
#         if cond.op == Kind.is_more_then:
#             r1 = get_register()
#             r2 = get_register()
#             r3 = get_register()
#
#             x = cond.x
#             y = cond.y
#
#             if x.type == Kind.number:
#                 codes.append('mov {} {}'.format(r1, x.value))
#             elif x.type == Kind.id:
#                 # todo
#                 codes.append('mov {} [{}]'.format(r1, x.value))
#             else:
#                 raise Exception('mov not type')
#
#             if y.type == Kind.number:
#                 codes.append('mov {} {}'.format(r2, y.value))
#
#             codes.append('comp {} {} {}'.format(r1, r2, r3))
#         else:
#             # todo
#             pass
#
#         l1 = get_label()
#         l2 = get_label()
#         l3 = get_label()
#         codes.append('cjmp {} {} {}'.format(r3, l1, l2))
#
#         codes.append('{}:'.format(l1))
#         gen_slist(inst.left)
#         codes.append('jmp {}'.format(l3))
#
#         codes.append('{}:'.format(l2))
#
#         gen_slist(inst.right)
#         codes.append('jmp {}'.format(l3))
#
#         codes.append('{}:'.format(l3))
#
#
# def gen_var(inst):
#     """
#
#     :param inst:
#     :return:
#     """
#     code = inst.left
#     # op = code.op
#
#     for c in code:
#         # r1 = get_register()
#         x = c.x
#         y = c.y
#         # stack.append(item.y.value)
#         # if len(y) > 1:
#         # r1 = get_register()
#         # r2 = get_register()
#         # r3 = get_register()
#         #
#         # codes.append('mov {} {}'.format(r1, item.x))
#         # codes.append('mov {} {}'.format(r2, item.y))
#         # codes.append('times {} {} {}'.format(r1, r2, r3))
#         #
#         # dest = get_register()
#         # codes.append('mov {} {}'.format(dest, r3))
#         f = True
#         for item in y:
#             op = item.op
#             if f:
#                 dest = get_register()
#                 codes.append('mov {} {}'.format(dest, item.y))
#                 f = False
#
#             if op == Kind.times:
#                 r1 = get_register()
#                 r2 = get_register()
#                 r3 = get_register()
#
#                 codes.append('mov {} {}'.format(r1, item.x))
#                 codes.append('mov {} {}'.format(r2, dest))
#                 codes.append('times {} {} {}'.format(r1, r2, r3))
#
#                 dest = get_register()
#                 codes.append('mov {} {}'.format(dest, r3))
#
#             elif op == Kind.plus:
#                 r1 = get_register()
#                 r2 = get_register()
#                 r3 = get_register()
#
#                 if isinstance(item.x, Quad):
#                     s1 = item.y
#                 else:
#                     s1 = item.x
#                 codes.append('mov {} {}'.format(r1, s1))
#                 codes.append('mov {} {}'.format(r2, dest))
#                 codes.append('plus {} {} {}'.format(r1, r2, r3))
#
#                 dest = get_register()
#                 codes.append('mov {} {}'.format(dest, r3))
#
#         codes.append('mov [{}] {}'.format(x.value, dest))
#
#
# def gen_print(inst):
#     """
#
#     :param inst:
#     :return:
#     """
#     code = inst.left
#     # op = code.op
#
#     for item in code:
#         # r1 = get_register()
#
#         if item.op == Kind.print:
#             # stack.append(item.y.value)
#             x = item.x
#             if x.type == Kind.id:
#                 codes.append('print [{}]'.format(x.value))
#             elif x.type == Kind.number:
#                 codes.append('print {}'.format(x.value))
#
#
# def gen_register_vm(ir):
#     instrs = ir.instrs
#
#     global codes
#     codes = []
#     for inst in instrs:
#         kind = inst.kind
#         if inst.kind == Kind.k_if:
#             gen_k_if(inst)
#
#         elif inst.kind == Kind.var:
#             gen_var(inst)
#
#         elif kind == Kind.print:
#             gen_print(inst)
#
#     return codes

register_index = 0
register_map = {}
db_index = 0
db_map = {}


class CodeRen(object):

    def __init__(self, ir):
        self.ir = ir
        self.index_register = 0
        self.index_label = 0
        self.codes = []
        # self.register_map = {}

    def gen_register(self, tmp_var=''):
        """
        tmp_var: 临时变量
        :return:
        """
        global register_index
        global register_map

        if tmp_var:
            # 存在临时变量
            r = register_map.get(tmp_var, None)
            if r is None:
                # 没有则生成并做映射
                r = 'r{}'.format(register_index)
                register_index += 1
                register_map.update({
                    tmp_var: r
                })
        else:
            r = 'r{}'.format(register_index)
            register_index += 1

        return r

    def gen_db(self, tmp_var=''):
        """
        数据区
        :param tmp_var:
        :return:
        """
        global db_index
        global db_map

        if tmp_var:
            # 存在临时变量
            r = db_map.get(tmp_var, None)
            if r is None:
                # 没有则生成并做映射
                r = 'db_{}'.format(db_index)
                db_index += 1
                db_map.update({
                    tmp_var: r
                })
        else:
            r = 'db_{}'.format(db_index)
            db_index += 1

        return r

    def get_label(self):
        """
        :return:
        """
        t = 'L{}'.format(self.index_label)
        self.index_label += 1

        return t

    def gen_var(self, ir):
        """

        :param ir:
        :return:
        """
        result = ir.result
        x = ir.x

        rx = self.gen_register(x)
        self.codes.append('mov [{}] {}'.format(result.value, rx))

    def gen_number(self, ir):
        """
        a = 122
        :param ir:
        :return:
        """
        result = ir.result
        x = ir.x

        rr = self.gen_register(result)

        self.codes.append('mov {} {}'.format(rr, x.value))

    def gen_times(self, ir):
        """
        r = a * b
        :param ir:
        :return:
        """
        result = ir.result
        x = ir.x
        y = ir.y

        rr = self.gen_register(result)
        rx = self.gen_register(x)
        ry = self.gen_register(y)

        self.codes.append('times {} {} {}'.format(rx, ry, rr))

    def gen_plus(self, ir):
        """
        r = a * b
        :param ir:
        :return:
        """
        result = ir.result
        x = ir.x
        y = ir.y

        rr = self.gen_register(result)
        rx = self.gen_register(x)
        ry = self.gen_register(y)

        self.codes.append('plus {} {} {}'.format(rx, ry, rr))

    def gen_print(self, ir):

        x = ir.value
        rx = self.gen_register(x)

        self.codes.append('print {}'.format(rx))

    def gen_id(self, ir):
        result = ir.result
        x = ir.x

        rr = self.gen_register(result)

        self.codes.append('mov {} [{}]'.format(rr, x.value))

    def gen_string(self, ir):

        result = ir.result
        x = ir.x

        rx = self.gen_register(result)

        self.codes.append('db {} {}'.format(rx, x.value))

    def gen_instr(self, ir):
        m = {
            Kind.var: self.gen_var,
            Kind.number: self.gen_number,
            Kind.times: self.gen_times,
            Kind.plus: self.gen_plus,
            Kind.id: self.gen_id,
            Kind.print: self.gen_print,
            Kind.string: self.gen_string,
            Kind.k_if: self.gen_kif,
            Kind.is_more_then: self.gen_is_more_then,
        }

        t = ir.type
        f = m.get(t, None)
        if f:
            f(ir)
        else:
            raise Exception('code gen_instr not found')


    def gen_kif(self, ir):

        cond = ir.condition
        listx = ir.x
        listy = ir.y

        rcond = self.gen_register(cond)
        l1 = self.get_label()
        l2 = self.get_label()
        l3 = self.get_label()
        self.codes.append('cjmp {} {} {}'.format(rcond, l1, l2))

        # l1
        self.codes.append('{}:'.format(l1))

        for x in listx:
            self.gen_instr(x)
        self.codes.append('jmp {}'.format(l3))

        # l2
        self.codes.append('{}:'.format(l2))
        for y in listy:
            self.gen_instr(y)
        self.codes.append('jmp {}'.format(l3))

        # l3
        self.codes.append('{}:'.format(l3))

    def gen_is_more_then(self, ir):
        """
        x > y  -> r
        :param ir:
        :return:
        """
        result = ir.result
        x = ir.x
        y = ir.y

        rr = self.gen_register(result)
        rx = self.gen_register(x)
        ry = self.gen_register(y)

        self.codes.append('cmp {} {} {}'.format(rx, ry, rr))

    def gen(self):
        m = {
            Kind.var: self.gen_var,
            Kind.number: self.gen_number,
            Kind.times: self.gen_times,
            Kind.plus: self.gen_plus,
            Kind.id: self.gen_id,
            Kind.print: self.gen_print,
            Kind.string: self.gen_string,
            Kind.k_if: self.gen_kif,
            Kind.is_more_then: self.gen_is_more_then,
        }

        for ir in self.ir:
            t = ir.type
            f = m.get(t, None)
            if f:
                f(ir)
            else:
                raise Exception('code gen not found')

        return self.codes
