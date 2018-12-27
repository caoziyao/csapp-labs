# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/29 
@desc:
"""

from compiler.backend.gen.opcodes import opcodes


class Assem(object):

    def label(self, label):
        return '{}:'.format(label)

    def call(self, dest):
        return 'call {}'.format(dest)

    def rrmovq(self, r1, r2):
        """
        r2 -> r1
        :param r1: 寄存器 r1
        :param r2: 寄存器 r2
        :return:
        """
        return 'rrmovq {} {}'.format(r1, r2)

    def irmovq(self, r1, im):
        """
        im -> r1
        :param r: 寄存器
        :param im: 立即数
        :return:
        """
        return 'irmovq {} {}'.format(r1, im)

    def imovq(self, number, memery):
        """
        im -> r1
        :param r: 寄存器
        :param im: 立即数
        :return:
        """
        return 'immovq {} {}'.format(memery, number)

    def rmmovq(self, memery, r1):
        """
        r1 -> memery
        :param memery: 内存地址
        :param r1: 寄存器
        :return:
        """
        return 'rmmovq {} {}'.format(memery, r1)

    def mrmovq(self, r1, memery):
        """
        memery -> r1
        :param r1:
        :param memery:
        :return:
        """
        return 'mrmovq {} {}'.format(r1, memery)

    def ret(self):
        """

        :return:
        """
        return 'ret'

    def jmp(self, dest):
        """
        jumps to dest unconditionaly
        :param dest:
        :return:
        """
        return 'jmp {}'.format(dest)

    def addq(self, dest, src1, src2):
        """
        addq dest src1 src2
        :param r1: 寄存器 r1
        :param r2: 寄存器 r2
        :param r2: 寄存器 r3
        :return:
        """
        return 'addq {} {} {}'.format(dest, src1, src2)

    def subq(self, dest, src1, src2):
        """
        subq dest src1 src2

        :param r1: 寄存器 r1
        :param r2: 寄存器 r2
        :param r2: 寄存器 r3
        :return:
        """
        return 'subq {} {} {}'.format(dest, src1, src2)

    # def cmp(self, src1, src2):
    #     """
    #     cmp src1 src2
    #     如果 src1 - src2 = 0 则 zf 置位
    #     src1 > src2  则 sf 置位
    #     :return:
    #     """
    #     return 'cmp {} {}'.format(src1, src2)

    def mrcmp(self, src1, src2):
        """
        memery reg
        cmp src1 src2
        如果 src1 - src2 = 0 则 zf 置位
        src1 > src2  则 sf 置位
        :return:
        """
        return 'mrcmp {} {}'.format(src1, src2)

    def micmp(self, src1, src2):
        """
        micmp memery number
        cmp src1 src2
        如果 src1 - src2 = 0 则 zf 置位
        src1 > src2  则 sf 置位
        :return:
        """
        return 'micmp {} {}'.format(src1, src2)

    def rrcmp(self, src1, src2):
        """
        reg reg
        cmp src1 src2
        如果 src1 - src2 = 0 则 zf 置位
        src1 > src2  则 sf 置位
        :return:
        """
        return 'rrcmp {} {}'.format(src1, src2)

    def ircmp(self, src1, src2):
        """
        ircmp number reg
        cmp src1 src2
        如果 src1 - src2 = 0 则 zf 置位
        src1 > src2  则 sf 置位
        :return:
        """
        return 'ircmp {} {}'.format(src1, src2)

    def rmcmp(self, src1, src2):
        """
        reg memery
        cmp src1 src2
        如果 src1 - src2 = 0 则 zf 置位
        src1 > src2  则 sf 置位
        :return:
        """
        return 'rmcmp {} {}'.format(src1, src2)

    def blt(self, tag):
        """
        | LT      | N不等于V               | 带符号数小于   |
        <
        ble tag
        如果 N不等于V，跳转
        :return:
        """
        return 'blt {} '.format(tag)

    def bgt(self, tag):
        """
        GT      | Z清零且（N等于V）     | 带符号数大于   |
        >
        bge tag
        如果 Z清零且（N等于V），跳转
        :return:
        """
        return 'bgt {} '.format(tag)