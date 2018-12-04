# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/12/3 
@desc:
reg:
0: r0
1: r1
2: r2
3: pc
4: sp

00000000
"""
import operator
from isa.constant import EErrorSignal, EWriteRead
from isa.instrutions import regfile


class CPU(object):

    def __init__(self):
        self.reg = [0] * 16  # 寄存器 16 个
        self.memory = bytearray(1024)  # 内存
        self.pc = 0
        self.regfile = regfile

    def load_memory(self, codes):
        """

        :return:
        """
        i = 0
        for c in codes:
            self.memory[i] = c
            i += 1

    def alu(self, a, b, op):
        """
        算术/逻辑单元
        operator:
        0123 -> +-*/

        Division	a / b	truediv(a, b)
        Division	a // b	floordiv(a, b)
        """
        m = {
            0: operator.add,
            1: operator.sub,
            2: operator.mul,
            3: operator.truediv,
        }

        if op not in m:
            raise Exception('not operatior')

        f = m[op]
        v = f(a, b)
        return v

    def read_register(self, srcA):
        """
        读寄存器 srcA(寄存器ID)
        :param srcA:
        :return:
        """
        return self.reg[srcA]

    def write_register(self, dstW, valW):
        """
        写寄存器
        valW(要写入的值) +  dstW(寄存器ID) -> 写入成功
        :return:
        """
        self.reg[dstW] = valW

    def hardware_register(self, srcA=None, dstW=None, valW=None, ):
        """
        hardware register
        硬件寄存器
        读端口，srcA(寄存器ID) -> valA(寄存器ID读出的值)
        写端口，valW(要写入的值) +  dstW(寄存器ID) -> 写入成功
        :return:
        """
        # 读
        if srcA is not None:
            return self.read_register(srcA)

        # 这里必须是写
        self.write_register(dstW, valW)

    def software_register(self):
        """
        software register
        软件寄存器
        :return:
        """
        pass

    def write_ram(self, address, val):
        """
        写 ram
        :return:
        """
        if address < len(self.memory):
            self.memory[address] = val
            err = EErrorSignal.success
        else:
            err = EErrorSignal.failure

        return err

    def read_ram(self, address):
        """
        读 ram
        :param address:
        :return:
        """
        if address < len(self.memory):
            val = self.memory[address]
            err = EErrorSignal.success
        else:
            err = EErrorSignal.failure
            val = None

        return err, val

    def hardware_ram(self, rw, address, val):
        """
        随机访问存储器
        输入：读/写（1/0），地址，数据输入，时钟
        输出：error (0/1)，数据输出
        :return:
        """
        if rw == 1:
            err = self.write_ram(address, val)
            res = None
        elif rw == 0:
            err, res = self.read_ram(address)
        else:
            raise Exception('error hardware_ram')

        if err == EErrorSignal.failure:
            raise Exception('over memery')

        # 返回读
        return res

    def read_memory(self, address):
        """
        :param address:
        :return:
        """
        if address >= len(self.memory):
            raise Exception('over memory')

        return self.memory[address]

    def run(self):
        """
        cpu run
        取指 fetch:
        译码 decode:
        执行 execute:
        放存 memory:
        写回 write back:
        更新pc pc update:
        :return:
        """
        regfile = self.regfile
        while True:
            code = self.read_memory(self.pc)
            if code not in regfile.keys():
                raise Exception('not opcode')

            if code == 0x21:
                self.instr_irmov()

    def instr_irmov(self):
        """
         irmov  $9  %rdx
        :param data:
        :return:
        """
        pc = self.pc

        # 取指
        code = self.read_memory(pc)
        r1 = self.read_memory(pc + 1)
        valc = self.read_memory(pc + 2)
        valpc = self.pc + 3

        # 译码

        # 执行
        vale = 0 + valc

        # 访存

        # 回写
        self.reg[r1] = vale

        # 更新 pc
        self.pc = valpc

    # def fetch(self):
    #     """
    #     取指 fetch
    #     :return:
    #     """
    #     pass
    #
    # def decode(self):
    #     pass
    #
    # def execute(self):
    #     pass
    #
    # def memory(self):
    #     pass
    #
    # def write_back(self):
    #     pass
    #
    # def pc_update(self):
    #     pass
