# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/29 
@desc:
"""


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

    def rmmovq(self, memery, r1):
        """
        r1 -> memery
        :param memery: 内存地址
        :param r1: 寄存器
        :return:
        """
        return 'rmmovq [{}] {}'.format(memery, r1)

    def mrmovq(self, r1, memery):
        """
        memery -> r1
        :param r1:
        :param memery:
        :return:
        """
        return 'mrmovq {} [{}]'.format(r1, memery)

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

    def addq(self, r1, r2, r3):
        """
        r1 + r2 -> r3
        todo: r1 + r2 -> r1
        :param r1: 寄存器 r1
        :param r2: 寄存器 r2
        :param r2: 寄存器 r3
        :return:
        """
        return 'addq {} {} {}'.format(r1, r2, r3)

    def subq(self, r1, r2, r3):
        """
        r1 - r2 -> r3
        todo: r1 - r2 -> r1
        :param r1: 寄存器 r1
        :param r2: 寄存器 r2
        :param r2: 寄存器 r3
        :return:
        """
        return 'subq {} {} {}'.format(r1, r2, r3)
