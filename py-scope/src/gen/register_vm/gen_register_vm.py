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
from .instruction import InstrY
from .assem import Assem

register_index = 0
register_map = {}
db_index = 0
db_map = {}
label_index = 0
label_map = {}


class CodeRen(object):

    def __init__(self, ir):
        self.ir = ir
        self.index_register = 0
        self.index_label = 0
        self.codes = []
        self.asm = Assem()

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

    def gen_label(self, label=''):
        global label_index
        global label_map

        if label:
            # 存在临时变量
            r = label_map.get(label, None)
            if r is None:
                # 没有则生成并做映射
                r = 'L{}'.format(label_index)
                label_index += 1
                label_map.update({
                    label: r
                })
        else:
            r = 'L{}'.format(label_index)
            label_index += 1

        return r

    def gen_var(self, ir):
        """

        :param ir:
        :return:
        """
        result = ir.result
        x = ir.x

        rx = self.gen_register(x)
        # self.codes.append('mov [{}] {}'.format(result.value, rx))
        self.emit(self.asm.rmmovq(result.value, rx))

    def gen_number(self, ir):
        """
        a = 122
        :param ir:
        :return:
        """
        result = ir.result
        x = ir.x

        rr = self.gen_register(result)

        self.emit(self.asm.irmovq(rr, x.value))
        # self.codes.append('mov {} {}'.format(rr, x.value))

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
        r = a + b
        :param ir:
        :return:
        """
        result = ir.result
        x = ir.x
        y = ir.y

        rr = self.gen_register(result)
        rx = self.gen_register(x)
        ry = self.gen_register(y)

        # self.codes.append('plus {} {} {}'.format(rx, ry, rr))
        self.emit(self.asm.addq(rx, ry, rr))

    def gen_minus(self, ir):
        """
        r = a - b
        :param ir:
        :return:
        """
        result = ir.result
        x = ir.x
        y = ir.y

        rr = self.gen_register(result)
        rx = self.gen_register(x)
        ry = self.gen_register(y)

        # self.codes.append('plus {} {} {}'.format(rx, ry, rr))
        self.emit(self.asm.subq(rx, ry, rr))

    def gen_print(self, ir):

        x = ir.value
        rx = self.gen_register(x)

        self.codes.append('print {}'.format(rx))

    def gen_id(self, ir):
        result = ir.result
        x = ir.x

        rr = self.gen_register(result)

        # self.codes.append('mov {} [{}]'.format(rr, x.value))
        self.emit(self.asm.mrmovq(rr, x.value))

    def gen_string(self, ir):

        result = ir.result
        x = ir.x

        rx = self.gen_register(result)

        self.codes.append('db {} {}'.format(rx, x.value))

    def emit(self, code):
        """
        生成代码
        :param code:
        :return:
        """
        self.codes.append(code)

    def gen_kif(self, ir):

        cond = ir.condition
        listx = ir.x
        listy = ir.y

        rcond = self.gen_register(cond)
        l1 = self.gen_label()
        l2 = self.gen_label()
        l3 = self.gen_label()
        self.codes.append('cjmp {} {} {}'.format(rcond, l1, l2))

        # l1
        self.emit(self.asm.label(l1))

        for x in listx:
            self.gen_instr(x)
        # self.codes.append('jmp {}'.format(l3))
        self.emit(self.asm.jmp(l3))

        # l2
        self.emit(self.asm.label(l2))

        for y in listy:
            self.gen_instr(y)
        # self.codes.append('jmp {}'.format(l3))
        self.emit(self.asm.jmp(l3))

        # l3
        self.emit(self.asm.label(l3))

    def gen_kwhile(self, ir):

        cond = ir.condition
        body = ir.body
        start = ir.start

        rcond = self.gen_register(cond)
        l1 = self.gen_label()
        l2 = self.gen_label()

        lstart = self.gen_label(start.label)

        self.codes.append('cjmp {} {} {}'.format(rcond, l1, l2))

        # l1
        self.emit(self.asm.label(l1))

        for x in body:
            self.gen_instr(x)

        # self.codes.append('jmp {}'.format(lstart))
        self.emit(self.asm.jmp(lstart))

        # l2
        self.emit(self.asm.label(l2))

    def gen_kwhile_start(self, ir):

        label = ir.label

        l1 = self.gen_label(label)
        self.emit(self.asm.label(l1))

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

        # self.codes.append('cmp {} {} {}'.format(rx, ry, rr))
        self.emit(self.asm.subq(rx, ry, rr))

    def gen_is_less_then(self, ir):
        """
        r1 - r2  -> r
        :param ir:
        :return:
        """
        result = ir.result
        x = ir.x
        y = ir.y

        rr = self.gen_register(result)
        rx = self.gen_register(x)
        ry = self.gen_register(y)

        # self.codes.append('cmp {} {} {}'.format(ry, rx, rr))
        self.emit(self.asm.subq(ry, rx, rr))

    def gen_undefind(self, ir):
        """
        未定义
        :param ir:
        :return:
        """
        result = ir.result
        x = ir.x

        rx = self.gen_register(result)

        self.codes.append('db {} {}'.format(rx, x.value))

    def gen_kdef_name(self, ir):

        func_name = ir.func_name

        # l1 = self.gen_label(func_name)
        self.codes.append('{}:'.format(func_name))

    def gen_kdef(self, ir):

        args = ir.args
        body = ir.body
        fname = ir.func_name

        # args
        for arg in args:
            self.gen_id(arg)

        # body
        for x in body:
            self.gen_instr(x)

        self.emit(self.asm.ret())

    def gen_call(self, ir):

        args = ir.args
        fname = ir.func_name

        # args
        for arg in args:
            self.gen_id(arg)

        dest = 'func_{}'.format(fname)
        cmd = self.asm.call(dest)
        self.codes.append(cmd)
        # self.codes.append('{} {}'.format(InstrY.call.value, l))

    def gen_instr(self, ir):
        m = {
            Kind.var: self.gen_var,
            Kind.number: self.gen_number,
            Kind.times: self.gen_times,
            Kind.plus: self.gen_plus,
            Kind.minus: self.gen_minus,
            Kind.id: self.gen_id,
            Kind.print: self.gen_print,
            Kind.string: self.gen_string,
            Kind.k_if: self.gen_kif,
            Kind.is_more_then: self.gen_is_more_then,
            Kind.is_less_then: self.gen_is_less_then,
            Kind.kwhile: self.gen_kwhile,
            Kind.kwhile_start: self.gen_kwhile_start,
            Kind.undefind: self.gen_undefind,
            Kind.kdef_name: self.gen_kdef_name,
            Kind.kdef: self.gen_kdef,
            Kind.call: self.gen_call,
            # Kind.kdef_end: self.gen_kdef_end,
        }
        t = ir.type
        f = m.get(t, None)
        if f:
            f(ir)
        else:
            raise Exception('code gen_instr not found')

    def gen(self):

        for ir in self.ir:
            self.gen_instr(ir)

        return self.codes
