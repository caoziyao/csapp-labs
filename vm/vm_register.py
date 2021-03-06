# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/26 
@desc:
"""
import sys
from vm.vm_state import VMState


def get_input(*args, **kw):
    """Read a string from standard input."""
    return input(*args, **kw)


class VM(object):

    def __init__(self, instrs):
        self.instrs = instrs
        self.memery = {}
        self.data = []
        self.table_label = {}
        self.stack = []
        self.current_inst = None
        self.status = VMState.idle
        self.R = [0] * 100
        self.zf = 0  # 当算术运算指令的目的操作数被赋 0 时，zf = 1
        self.sf = 0  # 在算术结果为负数时，sf = 1
        self.of = 0  # 有符号运算才有效，溢出时 of = 1
        self.cf = 0  # 无符号运算才有效，进位时 cf = 1
        self.rf = 0  # 自定义结果 0相等， 1大于  -1小于
        self.sp = 0
        self.pc = -1
        self.init()
        self.pc_start()

    def pop(self):

        return self.stack.pop()

    def push(self, value):

        self.stack.append(value)

    @property
    def R0(self):
        return self.R[0]

    @property
    def R1(self):
        return self.R[1]

    def init(self):

        self.init_table_label()

    def pc_start(self):
        for index, instr in enumerate(self.instrs):

            if instr == 'start:':
                self.pc = index - 1

    def init_table_label(self):
        """

        :return:
        """
        for index, instr in enumerate(self.instrs):
            if instr[0] == 'L':
                l = instr.split(':', 1)[0]
                self.table_label.update({
                    l: index
                })
            elif instr[:4] == 'func':
                l = instr.split(':', 1)[0]
                self.table_label.update({
                    l: index
                })

    def get_label_num(self, label):
        """
        获得 label
        :return:
        """
        t = self.table_label[label]
        return t

    # def op_cmp(self, *args):
    #
    #     src1 = args[1]
    #     src2 = args[2]
    #     dest = args[3]
    #
    #     r1 = self.value_from(src1)
    #     r2 = self.value_from(src2)
    #
    #     r = r1 - r2
    #     self.set_value(dest, r)

    def op_subq(self, *args):
        """
        subq dest src1 src2
        :param args:
        :return:
        """
        dest = args[1]
        src1 = args[2]
        src2 = args[3]

        # r
        idx1 = int(src1[1:])
        r1 = self.R[idx1]

        idx2 = int(src2[1:])
        r2 = self.R[idx2]

        # dest
        r = r1 - r2
        idx3 = int(dest[1:])
        self.R[idx3] = r
        # self.set_value(dest, r)

    # def value_from(self, src):
    #     """
    #     :param src:
    #     :return:
    #     """
    #     if self.is_memery(src):
    #         index = self.index_memery(src)
    #         r1 = self.memery[index]
    #     elif self.is_register(src):
    #         index = int(src[1:])
    #         r1 = self.R[index]
    #     else:
    #         r1 = int(src.strip())
    #
    #     return r1

    # def set_value(self, src, value):
    #     """
    #
    #     :return:
    #     """
    #     if self.is_memery(src):
    #         index = self.index_memery(src)
    #         self.memery[index] = value
    #
    #     elif self.is_register(src):
    #         index = int(src[1:])
    #         self.R[index] = value
    #     else:
    #         raise Exception('set_value error')

    def op_times(self, *args):
        """
        times dest src1 src2
        :param args:
        :return:
        """
        dest = args[1]
        src1 = args[2]
        src2 = args[3]

        # r
        idx1 = int(src1[1:])
        r1 = self.R[idx1]

        idx2 = int(src2[1:])
        r2 = self.R[idx2]

        # dest
        r = r1 * r2
        idx3 = int(dest[1:])
        self.R[idx3] = r

        # idx1 = int(src1[1:])
        # r1 = self.R[idx1]
        #
        # idx2 = int(src2[1:])
        # r2 = self.R[idx2]
        #
        #
        # # r1 = self.value_from(src1)
        # # r2 = self.value_from(src2)
        #
        # r = r1 * r2
        # self.set_value(dest, r)

    # def op_plus(self, *args):
    #     """
    #     addq dest src1 src2
    #     :param args:
    #     :return:
    #     """
    #     dest = args[1]
    #     src1 = args[2]
    #     src2 = args[3]
    #
    #     # r
    #     idx1 = int(src1[1:])
    #     r1 = self.R[idx1]
    #
    #     idx2 = int(src2[1:])
    #     r2 = self.R[idx2]
    #
    #     # dest
    #     r = r1 + r2
    #     idx3 = int(dest[1:])
    #     self.R[idx3] = r
    # src1 = args[1]
    # src2 = args[2]
    # dest = args[3]
    #
    # r1 = self.value_from(src1)
    # r2 = self.value_from(src2)
    #
    # r = r1 + r2
    # self.set_value(dest, r)

    def op_addq(self, *args):
        """
        addq dest src1 src2
        :param args:
        :return:
        """
        dest = args[1]
        src1 = args[2]
        src2 = args[3]

        # r
        idx1 = int(src1[1:])
        r1 = self.R[idx1]

        idx2 = int(src2[1:])
        r2 = self.R[idx2]

        # dest
        r = r1 + r2
        idx3 = int(dest[1:])
        self.R[idx3] = r
        # src1 = args[1]
        # src2 = args[2]
        # dest = args[3]
        #
        # idx1 = int(src1[1:])
        # r1 = self.R[idx1]
        #
        # idx2 = int(src2[1:])
        # r2 = self.R[idx2]
        #
        # # r1 = self.value_from(src1)
        # # r2 = self.value_from(src2)
        #
        # r = r1 + r2
        # self.set_value(dest, r)

    def op_jmp(self, *args):
        """

        :param args:
        :return:
        """
        l = args[1]

        self.set_pc(l)

    def read(self):
        self.push(get_input())

    def print(self, value):
        sys.stdout.write(str(value))
        sys.stdout.flush()

    def println(self, value):
        sys.stdout.write("{}\n".format(value))
        sys.stdout.flush()

    def op_print(self, *args):

        src = args[1]
        r = self.value_from(src)
        # print(r)
        self.println(r)

    def set_pc(self, label):
        """
        根据 lable 设置 跳转地址
        :param label:
        :return:
        """
        self.pc = self.get_label_num(label)

    # def op_cjmp(self, *args):
    #     """
    #     cjmp r1 l1 l2
    #     if r1 > 0: jmp l1
    #     if r1 < 0: jmp l2
    #     :param args:
    #     :return:
    #     """
    #     cond = args[1]
    #     l1 = args[2]
    #     l2 = args[3]
    #
    #     r = self.value_from(cond)
    #     if r > 0:
    #         self.set_pc(l1)
    #     else:
    #         self.set_pc(l2)

    def op_rrmovq(self, *args):
        """
        mrcmp src1 src2
        if r1 > 0: jmp l1
        if r1 < 0: jmp l2
        :param args:
        :return:
        """
        reg1 = args[1]
        reg2 = args[2]

        idx1 = int(reg1[1:])
        idx2 = int(reg2[1:])

        self.R[idx1] = self.R[idx2]

    def op_mrcmp(self, *args):
        """
        mrcmp src1 src2
        if r1 > 0: jmp l1
        if r1 < 0: jmp l2
        :param args:
        :return:
        """
        mem = args[1]
        reg = args[2]

        v1 = self.memery.get(mem)

        idx = int(reg[1:])
        v2 = self.R[idx]

        # 结果
        r = v1 - v2
        if r == 0:
            self.rf = 0
        elif r > 0:
            self.rf = 1
        else:
            self.rf = -1

        # r = self.value_from(cond)
        # if r > 0:
        #     self.set_pc(l1)
        # else:
        #     self.set_pc(l2)

    def op_rmcmp(self, *args):
        """
        rmcmp src1 src2
        if r1 > 0: jmp l1
        if r1 < 0: jmp l2
        :param args:
        :return:
        """
        reg = args[1]
        mem = args[2]

        v1 = self.memery.get(mem)

        idx = int(reg[1:])
        v2 = self.R[idx]

        # 结果
        r = v1 - v2
        if r == 0:
            self.rf = 0
        elif r > 0:
            self.rf = 1
        else:
            self.rf = -1

    def op_ircmp(self, *args):
        """
        ircmp src1 src2
        if r1 > 0: jmp l1
        if r1 < 0: jmp l2
        :param args:
        :return:
        """
        number = int(args[1])
        reg = args[2]

        v1 = number

        idx = int(reg[1:])
        v2 = self.R[idx]

        # 结果
        r = v1 - v2
        if r == 0:
            self.rf = 0
        elif r > 0:
            self.rf = 1
        else:
            self.rf = -1

    def op_blt(self, *args):
        """
        blt L0
        :param args:
        :return:
        """
        label = args[1]

        if self.rf == -1:
            self.set_pc(label)

    def op_ldrb(self, *args):
        pass

    # def is_register(self, r):
    #
    #     if isinstance(r, str):
    #         if r[0] == 'r':
    #             return True
    #
    #     return False

    # def is_memery(self, r):
    #
    #     if isinstance(r, str):
    #         if r[0] == '[':
    #             return True
    #
    #     return False

    def index_memery(self, code):
        """

        :param code:
        :return:
        """
        c = code.split('[', 1)[1].split(']')[0]
        return c

    # def op_mov(self, *args):
    #     dest = args[1]
    #     src1 = args[2]
    #
    #     r1 = self.value_from(src1)
    #
    #     self.set_value(dest, r1)

    def op_irmovq(self, *args):
        """
        irmovq dest src
        :param args:
        :return:
        """
        dest = args[1]
        src = int(args[2])

        index = int(dest[1:])
        self.R[index] = src

        # r1 = self.R[index]
        # r1 = self.value_from(src1)
        # index = int(src[1:])
        # self.set_value(dest, r1)

    def op_rmmovq(self, *args):
        """
        rmmovq dest src
        :param args:
        :return:
        """
        dest = args[1]
        src = args[2]

        index = int(src[1:])
        value = self.R[index]

        self.memery.update({
            dest: value
        })

        # value = self.value_from(src)
        # index = self.index_memery(dest)
        #         r1 = self.memery[index]

        # index = self.index_memery(src)
        # value = self.memery[index]

        # self.set_value(dest, r1)

    def op_mrmovq(self, *args):
        """
        mrmovq dest src
        :param args:
        :return:
        """
        reg = args[1]
        mem = args[2]

        idx = int(reg[1:])

        self.R[idx] = self.memery.get(mem)

    # def op_db(self, *args):
    #     dest = args[1]
    #     src1 = args[2]
    #
    #     self.set_value(dest, src1)

    def op_call(self, *args):
        func_name = args[1]

        self.push(self.pc)
        self.set_pc(func_name)
        # self.set_value(dest, src1)

    def op_ret(self, *args):
        # dest = args[1]
        # src1 = args[2]
        if self.stack:
            self.pc = self.pop()

        # self.set_value(dest, src1)

    def op_push(self, *args):

        pass

    def op_pop(self, *args):

        pass

    def next_instr(self):

        self.pc += 1

        l = len(self.instrs)
        if self.pc >= l - 1:
            self.status = VMState.idle

        instr = self.instrs[self.pc]

        return instr

    def args_from_instr(self, instr):
        """
        db r16 "www js"
        :param args:
        :return:
        todo
        """
        pass

    def run(self):
        """

        :param state:
        :return:
        """
        m = {
            # 'cmp': self.op_cmp,
            # 'plus': self.op_plus,
            # 'mov': self.op_mov,
            'irmovq': self.op_irmovq,
            'rmmovq': self.op_rmmovq,
            'mrmovq': self.op_mrmovq,
            'rrmovq': self.op_rrmovq,

            'mrcmp': self.op_mrcmp,
            'rmcmp': self.op_rmcmp,
            'ircmp': self.op_ircmp,

            'blt': self.op_blt,
            'addq': self.op_addq,

            'jmp': self.op_jmp,
            'times': self.op_times,

            # 'ldrb': self.op_ldrb,
            # 'subq': self.op_subq,
            # # 'cjmp': self.op_cjmp,
            # 'print': self.op_print,
            # 'push': self.op_push,
            # 'pop': self.op_pop,
            #

            # 'db': self.op_db,
            # 'call': self.op_call,
            # 'ret': self.op_ret,
        }

        self.status = VMState.run
        l = len(self.instrs)
        while True:
            if self.pc >= l - 1:
                break

            instr = self.next_instr()
            args = instr.split(' ')
            op = args[0]

            # label
            if op[0] == 'L':
                continue

            f = m.get(op)
            if f:
                f(*args)
            else:
                raise Exception('not fund {}'.format(instr))

        return self.R, self.memery
