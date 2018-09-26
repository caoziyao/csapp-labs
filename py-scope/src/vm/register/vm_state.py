# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/26 
@desc:
"""
from enum import Enum, unique


class VMInstr(object):

    def __init__(self, ip, flag, code, data):
        self.ip = ip  # 指令 prt
        self.flag = flag  # 记录最后判断的标志
        self.code = code  # 代码段地址
        self.data = data


@unique
class VMState(Enum):
    run = 0  # 运行
    idle = 1  # 空闲
