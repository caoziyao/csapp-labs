# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/26 
@desc:

{"mov",   MOV,   op_mov},
{"ldrb",  LDRB,  op_ldr},
{"ldr",   LDR,   op_ldr},
{"strb",  STRB,  op_str},
{"str",   STR,   op_str},

{"push",  PUSH,  op_push},
{"pop",   POP,   op_pop},

{"call",  CALL,  op_call},
{"ret",   RET,   op_ret},

{"add",   ADD,   op_alu},
{"sub",   SUB,   op_alu},
{"mul",   MUL,   op_alu},
{"div",   DIV,   op_alu},
{"and",   AND,   op_alu},
{"or",    OR,    op_alu},
{"xor",   XOR,   op_alu},
{"lol",   LOL,   op_alu},
{"lor",   LOR,   op_alu},

{"jmp",   JMP,   op_jmp},
{"jmpn",  JMPN,  op_jmp},
{"jmpz",  JMPZ,  op_jmp},
{"jmpo",  JMPO,  op_jmp},
{"jmpnn", JMPNN, op_jmp},
{"jmpnz", JMPNZ, op_jmp},
{"jmpno", JMPNO, op_jmp},

{"halt",  HALT,  op_halt},
"""
from src.common.expression import Kind
from src.vm.register.vm_state import VMState, VMInstr


#
# class VM(object):
#
#     def __init__(self, instrs):
#         self._instruction = {
#             'mov': self.op_mov,
#             'ldrb': self.op_ldrb,
#             'comp': self.op_comp,
#             'cjmp': self.op_cjmp,
#             'print': self.op_print,
#             'push': self.op_push,
#             'pop': self.op_pop,
#             'L': self.op_label,
#             'jmp': self.op_jmp,
#             'times': self.op_times,
#             'plus': self.op_plus,
#         }
#         self.instrs = instrs
#         self.stack = {}
#         self.data = []
#         self.table_label = {}
#         self.init()
#
#     @property
#     def R0(self):
#         return self.R[0]
#
#     @property
#     def R1(self):
#         return self.R[1]
#
#     def init(self):
#         self.pc = 0
#         self.current_inst = None
#         self.status = VMState.idle
#         self.R = [0] * 10
#         self.init_table_label()
#
#     def init_table_label(self):
#         """"""
#         for index, instr in enumerate(self.instrs):
#             op = instr[0]
#             if op[0] == 'L':
#                 self.op_label(instr, index)
#
#     # def update_table_label(self, lable, line):
#     #     """
#     #     :param lable: L1:  L2:
#     #     :param line: 行号:
#     #     :return:
#     #     """
#     #     l = 'L{}'.format(line)
#     #     self.table_label.update({
#     #         l: line
#     #     })
#
#     def get_label_num(self, label):
#         """
#         获得 label
#         :return:
#         """
#         t = self.table_label[label]
#         return t
#
#     def op_comp(self, *args):
#
#         src1 = args[1]
#         src2 = args[2]
#         dest = args[3]
#
#         r1 = int(src1[1])
#         r2 = int(src2[1])
#         r3 = int(dest[1])
#
#         self.R[r3] = self.R[r1] - self.R[r2]
#
#     def op_times(self, *args):
#
#         src1 = args[1]
#         src2 = args[2]
#         dest = args[3]
#
#         r1 = int(src1[1])
#         r2 = int(src2[1])
#         r3 = int(dest[1])
#
#         self.R[r3] = self.R[r1] * self.R[r2]
#
#     def op_plus(self, *args):
#
#         src1 = args[1]
#         src2 = args[2]
#         dest = args[3]
#
#         r1 = int(src1[1])
#         r2 = int(src2[1])
#         r3 = int(dest[1])
#
#         self.R[r3] = self.R[r1] + self.R[r2]
#
#     def op_jmp(self, *args):
#         src1 = args[1]
#
#         # r1 = int(src1[1])
#         self.pc = self.get_label_num(src1)
#
#     def op_print(self, *args):
#
#         src = args[1]
#
#         if '[' in src:
#             v = self.stack[src[1]]
#             print(v)
#         else:
#             print(src)
#
#         # self.pc = 10
#
#     def op_cjmp(self, *args):
#         cond = args[1]
#         l1 = args[2]
#         l2 = args[3]
#
#         r = int(cond[1])
#
#         if self.R[r] > 0:
#             self.pc = self.get_label_num(l1)
#         else:
#             self.pc = self.get_label_num(l2)
#
#     def op_ldrb(self, *args):
#         pass
#
#     def is_register(self, r):
#
#         if isinstance(r, str):
#             if r[0] == 'r':
#                 return True
#
#         return False
#
#     def is_memery(self, r):
#
#         if isinstance(r, str):
#             if r[0] == '[':
#                 return True
#
#         return False
#
#     def op_mov(self, *args):
#         # todo
#         r = args[1]
#
#         src = args[2]
#
#         if self.is_memery(r):
#             if self.is_register(src):
#                 self.stack[r[1]] = self.R[int(src[1])]
#             else:
#                 self.stack[r[1]] = int(src)
#         else:
#             if self.is_memery(src):
#                 number = self.stack[src[1]]
#
#                 rnum = int(r[1])
#                 self.R[rnum] = number
#             elif self.is_register(src):
#                 rnum = int(r[1])
#                 # self.R[rnum] = int(src)
#
#                 self.R[rnum] = self.R[int(src[1])]
#             else:
#                 rnum = int(r[1])
#                 if isinstance(src, str):
#                     src = src.strip()
#                 self.R[rnum] = int(src)
#
#     def op_push(self, *args):
#
#         pass
#
#     def op_pop(self, *args):
#
#         pass
#
#     def op_label(self, instr, number):
#         """
#         instr: L1:
#         :param instr:
#         :return:
#         """
#         l = instr.split(':', 1)[0]
#         self.table_label.update({
#             l: number
#         })
#
#     def next_instr(self):
#
#         instr = self.instrs[self.pc]
#         self.pc += 1
#
#         l = len(self.instrs)
#         if self.pc >= l:
#             self.status = VMState.idle
#
#         return instr
#
#     def run(self):
#         """
#
#         :param state:
#         :return:
#         """
#         self.status = VMState.run
#         while True:
#
#             if self.status == VMState.idle:
#                 break
#
#             instr = self.next_instr()
#             args = instr.split(' ')
#             op = args[0]
#             f = self._instruction.get(op)
#             if f:
#                 f(*args)


class VM(object):

    def __init__(self, instrs):
        self.instrs = instrs
        self.stack = {}
        self.data = []
        self.table_label = {}
        self.init()

    @property
    def R0(self):
        return self.R[0]

    @property
    def R1(self):
        return self.R[1]

    def init(self):
        self.pc = 0
        self.current_inst = None
        self.status = VMState.idle
        self.R = [0] * 100
        self.init_table_label()

    def init_table_label(self):
        """"""
        for index, instr in enumerate(self.instrs):
            op = instr[0]
            if op[0] == 'L':
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

    def op_cmp(self, *args):

        src1 = args[1]
        src2 = args[2]
        dest = args[3]

        r1 = self.value_from(src1)
        r2 = self.value_from(src2)

        r = r1 - r2
        self.set_value(dest, r)

    def value_from(self, src):
        """
        :param src:
        :return:
        """
        if self.is_memery(src):
            index = self.index_memery(src)
            r1 = self.stack[index]
        elif self.is_register(src):
            index = int(src[1:])
            r1 = self.R[index]
        else:
            r1 = int(src.strip())

        return r1

    def set_value(self, src, value):
        """

        :return:
        """
        if self.is_memery(src):
            index = self.index_memery(src)
            self.stack[index] = value

        elif self.is_register(src):
            index = int(src[1:])
            self.R[index] = value
        else:
            raise Exception('set_value error')

    def op_times(self, *args):

        src1 = args[1]
        src2 = args[2]
        dest = args[3]

        r1 = self.value_from(src1)
        r2 = self.value_from(src2)

        r = r1 * r2
        self.set_value(dest, r)

    def op_plus(self, *args):

        src1 = args[1]
        src2 = args[2]
        dest = args[3]

        r1 = self.value_from(src1)
        r2 = self.value_from(src2)

        r = r1 + r2
        self.set_value(dest, r)

    def op_jmp(self, *args):
        l = args[1]

        self.set_pc(l)
        # r1 = int(src1[1])
        # self.pc = self.get_label_num(src1)

    def op_print(self, *args):

        src = args[1]

        r = self.value_from(src)

        print(r)

        # if '[' in src:
        #     v = self.stack[src[1]]
        #     print(v)
        # else:
        #     print(src)

        # self.pc = 10

    def set_pc(self, label):
        """
        根据 lable 设置 跳转地址
        :param label:
        :return:
        """
        self.pc = self.get_label_num(label)

    def op_cjmp(self, *args):
        """
        cjmp r1 l1 l2
        if r1 > 0: jmp l1
        if r1 < 0: jmp l2
        :param args:
        :return:
        """
        cond = args[1]
        l1 = args[2]
        l2 = args[3]

        r = self.value_from(cond)
        if r > 0:
            self.set_pc(l1)
        else:
            self.set_pc(l2)

        # cond = args[1]
        # l1 = args[2]
        # l2 = args[3]
        #
        # r = int(cond[1])
        #
        # if self.R[r] > 0:
        #     self.pc = self.get_label_num(l1)
        # else:
        #     self.pc = self.get_label_num(l2)

    def op_ldrb(self, *args):
        pass

    def is_register(self, r):

        if isinstance(r, str):
            if r[0] == 'r':
                return True

        return False

    def is_memery(self, r):

        if isinstance(r, str):
            if r[0] == '[':
                return True

        return False

    def index_memery(self, code):
        """

        :param code:
        :return:
        """
        c = code.split('[', 1)[1].split(']')[0]
        return c

    def op_mov(self, *args):
        dest = args[1]
        src1 = args[2]

        r1 = self.value_from(src1)

        self.set_value(dest, r1)

    def op_db(self, *args):
        dest = args[1]
        src1 = args[2]

        self.set_value(dest, src1)

    def op_push(self, *args):

        pass

    def op_pop(self, *args):

        pass

    # def op_label(self, instr, number):
    #     """
    #     instr: L1:
    #     :param instr:
    #     :return:
    #     """
    #

    def next_instr(self):

        instr = self.instrs[self.pc]
        self.pc += 1

        l = len(self.instrs)
        if self.pc >= l:
            self.status = VMState.idle

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
            'mov': self.op_mov,
            'ldrb': self.op_ldrb,
            'cmp': self.op_cmp,
            'cjmp': self.op_cjmp,
            'print': self.op_print,
            'push': self.op_push,
            'pop': self.op_pop,
            'jmp': self.op_jmp,
            'times': self.op_times,
            'plus': self.op_plus,
            'db': self.op_db,
        }

        self.status = VMState.run
        while True:

            if self.status == VMState.idle:
                break

            instr = self.next_instr()
            args = instr.split(' ')
            op = args[0]
            f = m.get(op)
            if f:
                f(*args)

        return self.R, self.stack
