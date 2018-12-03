# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/12/3 
@desc:
"""
import operator
from isa.constant import EErrorSignal, EWriteRead


class CPU(object):

    def __init__(self):
        self.reg = [0] * 16  # 寄存器 16 个
        self.memory = [0] * 1024  # 内存

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

    def hardware_register(self, srcA=None, valW=None, dstW=None):
        """
        hardware register
        硬件寄存器
        读端口，srcA(寄存器ID) -> valA(寄存器ID读出的值)
        写端口，valW(要写入的值) +  dstW(寄存器ID) -> 写入成功
        :return:
        """
        # 读
        if srcA is not None:
            return self.reg[srcA]

        # 这里必须是写
        self.reg[dstW] = valW

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
