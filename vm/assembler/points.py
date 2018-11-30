# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/11/30 
@desc:
有符号数
byte 8bite
short 16bite
int 32bite
int64  64bite
"""
from vm.common.constant import EDataType

EData = {
    EDataType.byte: 8,
    EDataType.short: 16,
    EDataType.int: 32,
    EDataType.int64: 64,
}


def symbol(n):
    """
    符号位，0正，1负
    :param n:
    :return:
    """
    return '0' if n >= 0 else '1'


def significand(num, datatype=EDataType.byte):
    """
    尾数
    数字转换位二进制
    :return:
    """
    m = EData

    if datatype not in m:
        raise Exception('todo binary')

    b = m.get(datatype) - 1
    p = "{0:b}".format(abs(num))[-b:]

    return p


def gen_binary(num, datatype=EDataType.byte):
    """
    生成二进制
    :param num:
    :param datatype:
    :return:
    """

    # 符号位
    s = symbol(num)
    # 尾数
    p = significand(num, datatype)
    l = len(p)

    # 不足补 0
    n = EData.get(datatype) - 1
    if l <= n:
        p = s + '0' * (n - l) + p

    # encode
    p = p.encode()
    return p


def byte_point(n):
    """
    -127 ~ +127
    byte 8bite
    :param n:
    :return:
    """
    p = gen_binary(n, EDataType.byte)
    return p


def short_point(n):
    """
    short 16bite
    :param n:
    """
    p = gen_binary(n, EDataType.short)
    return p


def int_point(n):
    """
    short 32bite
    :param n:
    """
    p = gen_binary(n, EDataType.int)
    return p


def int64_point(n):
    """
    short 32bite
    :param n:
    """
    p = gen_binary(n, EDataType.int64)
    return p


def float_point():
    """
    单精度 32bit
    :return:
    """
    pass


def double_point():
    """
    双精度 64bit
    :return:
    """
    pass


if __name__ == '__main__':
    pass
