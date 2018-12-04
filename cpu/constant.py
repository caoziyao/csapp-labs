# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/12/3 
@desc:
"""
from enum import Enum, unique


class EWriteRead(Enum):
    read = 0
    write = 1


class EErrorSignal(Enum):
    success = 0
    failure = 1
