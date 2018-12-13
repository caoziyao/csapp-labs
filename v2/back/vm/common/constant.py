# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/11/30 
@desc:
"""

from enum import Enum, unique


@unique
class EDataType(Enum):
    """
    byte 8bite
    short 16bite
    int 32bite
    int64  64bite
    float 32bite
    double 64bite

    char * 32bite
    """
    byte = 0
    short = 1
    int = 2
    int64 = 3
    float = 4
    double = 5
