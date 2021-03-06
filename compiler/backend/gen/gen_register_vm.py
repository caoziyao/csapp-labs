# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/26 
@desc:
"""
# from lang.common import Kind
from enum import Enum
from compiler.common.tokentype import Type
from compiler.common.label_type import LabelType
from compiler.backend.gen.assem import Assem
from compiler.common.expression import Number, ID


class TypeArg(Enum):
    memery = 1
    regist = 2
    number = 3


class CodeRen(object):

    def __init__(self):
        # self.ir = ir
        self.idx_register = 0
        self.idx_label = 0
        self.idx_db = 0
        self.idx_label = 0
        self.label_map = {}
        self.register_map = {}
        self.db_map = {}
        self.codes = []
        self.asm = Assem()

    def gen_register(self, tmp_var=''):
        """
        tmp_var: 临时变量
        :return:
        """
        # global self.idx_register
        # global register_map

        if tmp_var:
            # 存在临时变量
            r = self.register_map.get(tmp_var, None)
            if r is None:
                # 没有则生成并做映射
                r = 'r{}'.format(self.idx_register)
                self.idx_register += 1
                self.register_map.update({
                    tmp_var: r
                })
        else:
            r = 'r{}'.format(self.idx_register)
            self.idx_register += 1

        return r

    def gen_db(self, tmp_var=''):
        """
        数据区
        :param tmp_var:
        :return:
        """
        # global db_index
        # global db_map

        if tmp_var:
            # 存在临时变量
            r = self.db_map.get(tmp_var, None)
            if r is None:
                # 没有则生成并做映射
                r = 'db_{}'.format(self.idx_db)
                self.idx_db += 1
                self.db_map.update({
                    tmp_var: r
                })
        else:
            r = 'db_{}'.format(self.idx_db)
            self.idx_db += 1

        return r

    def get_label(self, label=''):
        # global label_index
        # global label_map

        if label:
            # 存在临时变量
            r = self.label_map.get(label, None)
            if r is None:
                # 没有则生成并做映射
                r = 'L{}'.format(self.idx_label)
                self.idx_label += 1
                self.label_map.update({
                    label: r
                })
        else:
            r = 'L{}'.format(self.idx_label)
            self.idx_label += 1

        return r

    def type_of_arg(self, arg):
        """
        #0 寄存器
        id
        1
        :param arg:
        :return:
        """
        if isinstance(arg, ID):
            return TypeArg.memery

        else:
            if isinstance(arg, Number):
                return TypeArg.number
            else:
                return TypeArg.regist

    def gen_var(self, ir):
        """
        todo
        mov dest src
        :param ir:
        :return:
        """
        left = ir.arg1  # #0  left
        right = ir.arg2  # number  right

        ltype = self.type_of_arg(left)
        rtype = self.type_of_arg(right)

        if rtype == TypeArg.memery:
            # 右值是 Id
            rv = right.value
            if ltype == TypeArg.regist:
                lv = self.gen_register(left)
                self.emit(self.asm.mrmovq(lv, rv))

        if rtype == TypeArg.regist:
            # 右值是 寄存器
            rv = self.gen_register(right)

            if ltype == TypeArg.regist:
                lv = self.gen_register(left)
                self.emit(self.asm.rrmovq(lv, rv))

            if ltype == TypeArg.memery:
                lv = left.value
                self.emit(self.asm.rmmovq(lv, rv))

        if rtype == TypeArg.number:
            # 右值是 立即数
            rv = right

            if ltype == TypeArg.regist:
                # 左值是寄存器
                lv = self.gen_register(left)
                self.emit(self.asm.irmovq(lv, rv))
            if ltype == TypeArg.memery:
                # 左值是 memery
                lv = left.value
                self.emit(self.asm.imovq(lv, rv))

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
        times dest src1 src2
        :param ir:
        :return:
        """
        result = ir.result
        x = ir.x
        y = ir.y

        rr = self.gen_register(result)
        rx = self.gen_register(x)
        ry = self.gen_register(y)

        self.codes.append('times {} {} {}'.format(rr, rx, ry))

    def gen_plus(self, ir):
        """
        addq dest src1 src2
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
        self.emit(self.asm.addq(rr, rx, ry))

    def gen_sub(self, ir):
        """
        subq dest src1 src2
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
        self.emit(self.asm.subq(rr, rx, ry))

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

    def gen_more_then(self, ir):
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

    def gen_less_then(self, ir):
        """
        left < right
        :param ir:
        :return:
        """
        left = ir.arg1
        right = ir.arg2

        ltype = self.type_of_arg(left)
        rtype = self.type_of_arg(right)

        if ltype == TypeArg.memery:
            lv = left.value

            if rtype == TypeArg.regist:
                rv = self.gen_register(right)
                self.emit(self.asm.mrcmp(lv, rv))

            if rtype == TypeArg.number:
                rv = right
                self.emit(self.asm.micmp(lv, rv))

        if ltype == TypeArg.regist:
            lv = self.gen_register(left)

            if rtype == TypeArg.regist:
                rv = self.gen_register(right)
                self.emit(self.asm.rrcmp(lv, rv))


        if ltype == TypeArg.number:
            lv = left

            if rtype == TypeArg.regist:
                rv = self.gen_register(right)
                self.emit(self.asm.ircmp(lv, rv))


        # if isinstance(left, ID):
        #     rr = self.gen_register(right)
        #     self.emit(self.asm.mrcmp(left.value, rr))
        # else:
        #     rl = self.gen_register(left)
        #     rr = self.gen_register(right)
        #     self.emit(self.asm.rrcmp(rl, rr))

        # rr = self.gen_register(result)
        # rx = self.gen_register(x)
        # ry = self.gen_register(y)
        #
        # # self.codes.append('cmp {} {} {}'.format(ry, rx, rr))
        # self.emit(self.asm.subq(ry, rx, rr))

    def gen_goto(self, ir):
        """
        goto label
        :param ir:
        :return:
        """
        label = ir.label
        # cond = ir.condition

        # _type = cond.type
        l = self.get_label(label)

        self.emit(self.asm.jmp(l))
        # if _type == Type.less_then:
        #     self.emit(self.asm.blt(l))
        #
        # elif _type == Type.more_then:
        #     self.emit(self.asm.bgt(l))

    def gen_cmdgoto(self, ir):
        """
        goto label
        :param ir:
        :return:
        """
        label = ir.label
        cond = ir.condition

        _type = cond.op
        l = self.get_label(label)

        if _type == Type.less_then:
            self.emit(self.asm.blt(l))

        elif _type == Type.more_then:
            self.emit(self.asm.bgt(l))

    def gen_label(self, ir=None):
        """
        lable
        :param ir:
        :return:
        """
        l = self.get_label(ir.label)
        self.emit(self.asm.label(l))

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
            # Kind.var: self.gen_var,
            # Kind.number: self.gen_number,
            # Kind.times: self.gen_times,
            # Kind.plus: self.gen_plus,
            # Kind.sub: self.gen_sub,
            # Kind.id: self.gen_id,
            # Kind.print: self.gen_print,
            # Kind.string: self.gen_string,
            # Kind.k_if: self.gen_kif,
            # Kind.is_more_then: self.gen_more_then,
            # Kind.is_less_then: self.gen_less_then,
            # Kind.kwhile: self.gen_kwhile,
            # Kind.kwhile_start: self.gen_kwhile_start,
            # Kind.undefind: self.gen_undefind,
            # Kind.kdef_name: self.gen_kdef_name,
            # Kind.kdef: self.gen_kdef,
            # Kind.call: self.gen_call,
            # Kind.kdef_end: self.gen_kdef_end,
            LabelType.whilestart: self.gen_kwhile_start,
            LabelType.kdef_name: self.gen_kdef_name,

            # Keywords.kdef: self.gen_kdef,
            # Keywords.call: self.gen_call,
            # # Keywords.var: self.gen_var,
            # Keywords.print: self.gen_print,
            # Keywords.kif: self.gen_kif,
            # Keywords.kwhile: self.gen_kwhile,
            # Keywords.undefind: self.gen_undefind,

            Type.assign: self.gen_var,
            Type.number: self.gen_number,
            Type.times: self.gen_times,
            Type.add: self.gen_plus,
            Type.sub: self.gen_sub,
            Type.id: self.gen_id,
            Type.string: self.gen_string,
            Type.more_then: self.gen_more_then,
            Type.less_then: self.gen_less_then,
            Type.goto: self.gen_goto,
            Type.cmdgoto: self.gen_cmdgoto,
            LabelType.label: self.gen_label,

        }
        t = ir.op
        f = m.get(t, None)
        if f:
            f(ir)
        else:
            raise Exception('code gen_instr not found')

    def gen(self, irs):

        for ir in irs:
            self.gen_instr(ir)

        return self.codes
