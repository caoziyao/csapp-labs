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


class VM(object):

    def __init__(self, instrs):
        self._instruction = {
            'mov': self.op_mov,
            'ldrb': self.op_ldrb,
            'comp': self.op_comp,
            'cjmp': self.op_cjmp,
            'print': self.op_print,
        }
        self.instrs = instrs
        self.stack = []
        self.data = []
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
        self.R = [0] * 10

    def op_comp(self, *args):

        src1 = args[1]
        src2 = args[2]
        dest = args[3]

        r1 = int(src1[1])
        r2 = int(src2[1])
        r3 = int(dest[1])

        self.R[r3] = self.R[r1] - self.R[r2]

    def op_print(self, *args):

        value = args[1]

        print(value)

        self.pc = 8

    def op_cjmp(self, *args):
        cond = args[1]
        r = int(cond[1])

        if self.R[r] > 0:
            self.pc = 4
        else:
            self.pc = 6

    def op_ldrb(self, *args):
        pass

    def op_mov(self, *args):

        r = args[1]
        src = int(args[2])
        rnum = int(r[1])
        self.R[rnum] = src

    def next_instr(self):

        instr = self.instrs[self.pc]
        self.pc += 1

        l = len(self.instrs)
        if self.pc >= l:
            self.status = VMState.idle

        return instr

    def run(self):
        """

        :param state:
        :return:
        """
        self.status = VMState.run
        while True:

            if self.status == VMState.idle:
                break

            instr = self.next_instr()
            args = instr.split(' ')
            op = args[0]
            f = self._instruction.get(op)
            if f:
                f(*args)
