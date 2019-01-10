# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/12/27 
@desc:
"""
from enum import Enum, unique


@unique
class OpMode(Enum):
    IABC = 0  # [B:9][C: 9][A: 8][OP: 6]
    IABx = 1  # [Bx: 18][A: 8][OP: 6]
    IAsBx = 2  # [sBx: 18][A: 8][OP: 6]
    IAx = 3  # [Ax:26][OP:6]


@unique
class OpArg(Enum):
    OpArgN = 0  # 未被使用
    OpArgU = 1  # 操作数被使用(立即数?)
    OpArgR = 2  # 寄存器或者跳转的偏移量
    OpArgK = 3  # 寄存器或者常量


class Opcodes(object):

    def __init__(self, code=0, name='', testFlag=0, mode=None):
        self.testFlag = testFlag
        self.mode = mode
        self.name = name
        self.code = code
        self.a = None
        self.b = None
        self.c = None

    def opmode(self):
        self.opmode = {
            'mov': ''
        }


def gen_code(mode, a, b, c):
    """
    :return:
    """
    if mode == OpMode.IABC:
        _format = b'{code}{a}{b}{c}'
    elif mode == OpMode.IABx:
        _format = b'{code}{a}{b}{c}'


def gen_mov(name, a, b):
    """
    irmovq r0 10
    :param a:
    :param b:
    :return:
    """
    opcodes.get(name)


# code, opmode, b, c
opcodes = {
    'irmovq': [0x20, ]
}
